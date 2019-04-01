from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import app, ctrl, clip, ui
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

from talon.engine import engine

engine.register("ready", lambda j: engine.cmd("g.update", name="dragon", enabled=False))

# cleans up some Dragon output from <dgndictation>
mapping = {
    "semicolon": ";",
    "new-line": "\n",
    "new-paragraph": "\n\n",
    "furnish": "varnish",
    "pseudo-": "sudo",
    "apt get": "apt-get",
    "krohn": "cron",
    "standard out": "stdout",
    "standard in": "stdin",
    "standard error": "stderr",
    "keep": "key",
    "keeper": "key",
    "crum": "chrome",
    "crump": "chrome",
    "laugh": "waf",
    "pearl": "perl",
    "cash": "cache",
    "gage": "gauge",
    "scaler": "scalar",
    "warren": "warn",
    "worn": "warn",
    "carl": "curl",
    "bcl": "vcl",
    "tubal": "tuple",
    "vastly": "fastly",
}

# used for auto-spacing
punctuation = set(".,-!?")


def parse_word(word):
    word = str(word).lstrip("\\").split("\\", 1)[0]
    word = mapping.get(word.lower(), word)
    return word


def join_words(words, sep=" "):
    out = ""
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += word
    return out


def parse_words(m):
    return list(map(parse_word, m.dgndictation[0]._words))


def insert(s):
    Str(s)(None)


def text(m):
    insert(join_words(parse_words(m)).lower())


def sentence_text(m):
    text = join_words(parse_words(m)).lower()
    insert(text.capitalize())


def word(m):
    text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
    insert(text.lower())


def surround(by):
    def func(i, word, last):
        if i == 0:
            word = by + word
        if last:
            word += by
        return word

    return func


def rot13(i, word, _):
    out = ""
    for c in word.lower():
        if c in string.ascii_lowercase:
            c = chr((((ord(c) - ord("a")) + 13) % 26) + ord("a"))
        out += c
    return out


formatters = {
    "dunder": (True, lambda i, word, _: "__%s__" % word if i == 0 else word),
    "camel": (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    "snake": (True, lambda i, word, _: word if i == 0 else "_" + word),
    "smash": (True, lambda i, word, _: word),
    # spinal or kebab?
    "kebab": (True, lambda i, word, _: word if i == 0 else "-" + word),
    "pack": (True, lambda i, word, _: word if i == 0 else "::" + word),
    # 'sentence':  (False, lambda i, word, _: word.capitalize() if i == 0 else word),
    "title": (False, lambda i, word, _: word.capitalize()),
    "allcaps": (False, lambda i, word, _: word.upper()),
    "dubstring": (False, surround('"')),
    "string": (False, surround("'")),
    "padded": (False, surround(" ")),
    "rot-thirteen": (False, rot13),
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
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words) - 1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = " "
    if not spaces:
        sep = ""
    Str(sep.join(words))(None)


def copy_bundle(m):
    bundle = ui.active_app().bundle
    clip.set(bundle)
    app.notify("Copied app bundle", body="{}".format(bundle))


ctx = Context("standard")

ctx.vocab = [
    "docker",
    "talon",
    "pragma",
    "pragmas",
    "vim",
    "configs",
    "spotify",
    "upsert",
]

keymap = {}
keymap.update(
    {
        "(phrase | say) <dgndictation> [over]": text,
        "sentence <dgndictation> [over]": sentence_text,
        "comma <dgndictation> [over]": [", ", text],
        "period <dgndictation> [over]": [". ", sentence_text],
        "more <dgndictation> [over]": [" ", text],
        "word <dgnwords>": word,
        "(%s)+ <dgndictation> [over]" % (" | ".join(formatters)): FormatText,
        "slap": [Key("cmd-right enter")],
        "cd": "cd ",
        "cd talon home": "cd {}".format(TALON_HOME),
        "cd talon user": "cd {}".format(TALON_USER),
        "cd talon plugins": "cd {}".format(TALON_PLUGINS),
        "grep": "grep ",
        "(rm | are em)": "rm",
        "elle less": "ls ",
        "run L S": "ls\n",
        "run (S S H | S H)": "ssh",
        "(ssh | sh)": "ssh ",
        "ack": "ack ",
        "diff": "diff ",
        "dot pie": ".py",
        "run vim": "vim ",
        "run make": "make\n",
        "run jobs": "jobs\n",
        "run make (durr | dear)": "mkdir ",
        "(jay son | jason )": "json",
        "(http | htp)": "http",
        "tls": "tls",
        "md5": "md5",
        "(regex | rejex)": "regex",
        "const": "const ",
        "static": "static ",
        "tip pent": "int ",
        "tip char": "char ",
        "tip byte": "byte ",
        "tip pent 64": "int64_t ",
        "tip you went 64": "uint64_t ",
        "tip pent 32": "int32_t ",
        "tip you went 32": "uint32_t ",
        "tip pent 16": "int16_t ",
        "tip you went 16": "uint16_t ",
        "tip pent 8": "int8_t ",
        "tip you went 8": "uint8_t ",
        "tip size": "size_t",
        "tip float": "float ",
        "tip double": "double ",
        "args": ["()", Key("left")],
        "(index | array)": ["[]", Key("left")],
        "block": ["{}", Key("left enter enter up tab")],
        "empty array": "[]",
        "empty dict": "{}",
        "state (def | deaf | deft)": "def ",
        "state else if": "elif ",
        "state if": "if ",
        "state else if": [" else if ()", Key("left")],
        "state while": ["while ()", Key("left")],
        "state for": ["for ()", Key("left")],
        "state for": "for ",
        "state switch": ["switch ()", Key("left")],
        "state case": ["case \nbreak;", Key("up")],
        "state goto": "goto ",
        "state import": "import ",
        "state class": "class ",
        "state include": "#include ",
        "state include system": ["#include <>", Key("left")],
        "state include local": ['#include ""', Key("left")],
        "state type deaf": "typedef ",
        "state type deaf struct": ["typedef struct {\n\n};", Key("up"), "\t"],
        "comment see": "// ",
        "comment py": "# ",
        "word queue": "queue",
        "word eye": "eye",
        "word bson": "bson",
        "word iter": "iter",
        "word no": "NULL",
        "word cmd": "cmd",
        "word dup": "dup",
        "word streak": ["streq()", Key("left")],
        "word printf": "printf",
        "word (dickt | dictionary)": "dict",
        "word shell": "shell",
        "word Point2d": "Point2d",
        "word Point3d": "Point3d",
        "title Point": "Point",
        "word angle": "angle",
        "dunder in it": "__init__",
        "self taught": "self.",
        "dickt in it": ["{}", Key("left")],
        "list in it": ["[]", Key("left")],
        "string utf8": "'utf8'",
        "state past": "pass",
        "shebang bash": "#!/bin/bash -u\n",
        "new window": Key("cmd-n"),
        "next window": Key("cmd-`"),
        "last window": Key("cmd-shift-`"),
        # 'next app': Key('cmd-tab'),
        # 'last app': Key('cmd-shift-tab'),
        "next tab": Key("ctrl-tab"),
        "new tab": Key("cmd-t"),
        "last tab": Key("ctrl-shift-tab"),
        "next space": Key("cmd-alt-ctrl-right"),
        "last space": Key("cmd-alt-ctrl-left"),
        "zoom [in]": Key("cmd-+"),
        "zoom out": Key("cmd--"),
        "(page | scroll) up": Key("pgup"),
        "(page | scroll) [down]": Key("pgdown"),
        "copy": Key("cmd-c"),
        "cut": Key("cmd-x"),
        "paste": Key("cmd-v"),
        "flock off": Key("escape"),
        "menu help": Key("cmd-shift-?"),
        "spotlight": Key("cmd-space"),
        "(undo | under | skunks)": Key("cmd-z"),
        "redo": Key("cmd-shift-z"),
        "(crap | clear | scratch )": Key("cmd-backspace"),
        "more bright": Key("brightness_up"),
        "less bright": Key("brightness_down"),
        "volume up": Key("volume_up"),
        "volume down": Key("volume_down"),
        "mute": Key("mute"),
        "play next": Key("next"),
        "play previous": Key("previous"),
        "(play | pause)": Key("space"),  # spotify
        "copy active bundle": copy_bundle,
        "wipe": Key("backspace"),
        "(pad | padding ) ": ["  ", Key("left")],
    }
)

ctx.keymap(keymap)
