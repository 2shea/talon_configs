from talon import clip
from talon.voice import Context, press
from talon.webview import Webview
from .utils import parse_word

context = Context("picker")
webview = Webview()

css_template = """
<style type="text/css">
body {
    padding: 0;
    margin: 0;
    font-size: 150%;
    min-width: 600px;
}

td {
    text-align: left;
    margin: 0;
    padding: 5px 10px;
}

h3 {
    padding: 5px 0px;
}

table {
    counter-reset: rowNumber;
}

table .count {
    counter-increment: rowNumber;
}

.count td:first-child::after {
    content: counter(rowNumber);
    min-with: 1em;
    margin-right: 0.5em;
}

.pick {
    font-weight: normal;
    font-style: italic;
}

.cancel {
    text-align: center;
}

</style>
"""

template = (
    css_template
    + """
<div class="contents">
<h3>{{ title }}</h3>
<table>
{% for line in data %}
<tr class="count"><td class="pick">🔊 pick </td><td>{{ line }}</td></tr>
{% endfor %}
<tr><td colspan="2" class="pick cancel">🔊 cancel</td></tr>
</table>
</div>
"""
)


def selection_picker(title, data, keymap={}):
    picker = Picker(title=title, data=data, keymap=keymap)
    picker.render()


class Picker:
    def __init__(self, title, data, keymap):
        self.title = title
        self.data = data
        self.keymap = keymap

        self.keymap.update(
            {
                "[pick] %s" % (i + 1): lambda m: self.make_selection(m)
                for i in range(len(self.data))
            }
        )
        self.keymap.update({"(cancel | 0)": lambda _: self.close()})

    def make_selection(self, m):
        words = m._words
        selection = int(parse_word(words[1]))
        clip.set(self.data[selection - 1])
        press("cmd-v", wait=2000)
        self.close()

    def render(self):
        if len(self.data) == 0:
            return
        webview.render(template, title=self.title, data=self.data)
        webview.show()
        context.keymap(self.keymap)
        context.load()

    def close(self):
        webview.hide()
        context.unload()
