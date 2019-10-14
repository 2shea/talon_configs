import os
import itertools
from atomicwrites import atomic_write
from collections import deque

from talon import app, webview

from talon.engine import engine
from talon_init import TALON_HOME
from talon.voice import Context
from ..utils import optional_numerals, text_to_number

context = Context("history")

path = os.path.join(TALON_HOME, "last_phrase")
WEBVIEW = True
FONT_SIZE = 12
BORDER_SIZE = int(FONT_SIZE / 6)
NOTIFY = False
LAST_COUNT = 5
LAST_MAX = 50

css_template = (
    """
<style type="text/css">
    body {
        padding: 0;
        margin: 0;
        font-size: """
    + str(FONT_SIZE)
    + """px;
        -webkit-border-vertical-spacing: """
    + str(BORDER_SIZE)
    + """px;
        -webkit-border-horizontal-spacing: """
    + str(BORDER_SIZE)
    + """px;
    }

    .contents {
        width: 100%;
    }

    td {
        text-align: left;
        margin: 0;
        padding: 0;
        padding-left: 5px;
        width: 1px;
        white-space: nowrap;
    }

</style>
"""
)

last_template = (
    css_template
    + """
    <style type="text/css">
        tr:first-child { background: black; color: white; }
    </style>
    <div class="contents">
    <table>
    {% for phrase in last_items %}
        <tr><td>{{ phrase }}</td></tr>
    {% endfor %}
    </table>
    </div>
"""
)


if WEBVIEW:
    webview = webview.Webview()
    webview.body = "<i>[waiting&nbsp;for&nbsp;phrase]</i>"
    # webview.show()
    # only use a deque for the webview
    last_items = deque(maxlen=LAST_MAX)


def parse_phrase(phrase):
    return " ".join(word.split("\\")[0] for word in phrase)


def on_phrase(j):
    global LAST_COUNT
    phrase = parse_phrase(j.get("phrase", []))
    cmd = j["cmd"]
    if cmd == "p.end":

        if phrase:
            with atomic_write(path, overwrite=True) as f:
                f.write(phrase)

            if WEBVIEW:
                last_items.appendleft(phrase)
                phrase_words = phrase.split()

                if "history show" in phrase and phrase_words[-1].isdigit():
                    LAST_COUNT = int(phrase_words[-1])

                webview.render(last_template, last_items=list(itertools.islice(last_items, 0, LAST_COUNT)))

            if NOTIFY:
                app.notify(body=phrase)


engine.register("phrase", on_phrase)


def close_history():
    webview.hide()


def open_history():
    webview.show()


context.keymap(
    {
        "history (close | hide)": lambda _: close_history(),
        "history (open | show)" + optional_numerals(): lambda _: open_history(),
    }
)
