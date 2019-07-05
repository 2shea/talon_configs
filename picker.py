import os
import io
from talon import clip
from talon.voice import Context, press
from talon.webview import Webview
from .utils import parse_word

context = Context("picker")
webview = Webview()

MODULE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(MODULE_DIRECTORY, "picker.css")) as f:
    css_template = f.read()

with io.open(os.path.join(MODULE_DIRECTORY, "picker.html"), "r", encoding="utf8") as f:
    html_template = f.read()

template = '<style type="text/css">' + css_template + "</style>" + html_template


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
