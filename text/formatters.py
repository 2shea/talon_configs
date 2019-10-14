from talon.voice import Word, Context, Key, Str, press
from talon import app, clip, ui
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string
from ..utils import surround, parse_words, parse_word, sentence_text, text, word

ctx = Context("formatters")

formatters = {
    "dunder": (True, lambda i, word, _: "__%s__" % word if i == 0 else word),
    "camel": (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    "snake": (True, lambda i, word, _: word.lower() if i == 0 else "_" + word.lower()),
    "smash": (True, lambda i, word, _: word),
    "kebab": (True, lambda i, word, _: word if i == 0 else "-" + word),
    "pack": (True, lambda i, word, _: word if i == 0 else "::" + word),
    "title": (False, lambda i, word, _: word.capitalize()),
    "allcaps": (False, lambda i, word, _: word.upper()),
    "alldown": (False, lambda i, word, _: word.lower()),
    "dubstring": (False, surround('"')),
    "string": (False, surround("'")),
    "padded": (False, surround(" ")),
    "dotted": (True, lambda i, word, _: word if i == 0 else "." + word),
    "slasher": (True, lambda i, word, _: "/" + word),
}

def FormatText(m):
    fmt = []
    if m._words[-1] == "over":
        m._words = m._words[:-1]
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    try:
        words = parse_words(m)
    except AttributeError:
        with clip.capture() as s:
            press("cmd-c")
        words = s.get().split(" ")
        if not words:
            return

    tmp = []
    spaces = True
    for i, w in enumerate(words):
        w = parse_word(w)
        for name in reversed(fmt):
            smash, func = formatters[name]
            w = func(i, w, i == len(words) - 1)
            spaces = spaces and not smash
        tmp.append(w)
    words = tmp

    sep = " "
    if not spaces:
        sep = ""
    Str(sep.join(words))(None)

keymap = {}
keymap.update(
    {
        "phrase <dgndictation> [over]": text,
        "(say | speak) <dgndictation>++ [over]": text,
        "sentence <dgndictation> [over]": sentence_text,
        "word <dgnwords>": word,
        "(%s)+ <dgndictation> [over]" % (" | ".join(formatters)): FormatText,
    }
)

ctx.keymap(keymap)


