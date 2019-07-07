import os
from atomicwrites import atomic_write
from collections import deque
from talon import app, webview, ui
from talon.engine import engine
from talon_init import TALON_HOME
from talon.voice import Context

context = Context("history")

path = os.path.join(TALON_HOME, "last_phrase")
WEBVIEW = True
FONT_SIZE = 50
BORDER_SIZE = int(FONT_SIZE / 6)
NOTIFY = False
LAST_COUNT = 3


main = ui.main_screen().visible_rect
main.width

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
        width: """
    + str(main.width)
    + """px;
    }

    td {
        text-align: left;
        margin: 0;
        padding: 0;
        padding-left: 15px;
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
    # webview.resize(x=main.x, y=main.y, w=main.width, h=main.height)
    # webview.show()
    # only use a deque for the webview
    last_items = deque(maxlen=LAST_COUNT)


def parse_phrase(phrase):
    return " ".join(word.split("\\")[0] for word in phrase)


def on_phrase(j):
    phrase = parse_phrase(j.get("phrase", []))
    cmd = j["cmd"]
    if cmd == "p.end":

        if phrase:
            with atomic_write(path, overwrite=True) as f:
                f.write(phrase)

            if WEBVIEW:
                last_items.appendleft(phrase)
                webview.render(last_template, last_items=last_items)

            if NOTIFY:
                app.notify(body=phrase)


engine.register("phrase", on_phrase)


def close_history():
    webview.hide()


def open_history():
    webview.show()


context.keymap(
    {
        "history (close | hide)": lambda x: close_history(),
        "history (open | show)": lambda x: open_history(),
    }
)
