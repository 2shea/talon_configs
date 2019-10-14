from talon.voice import Word, Context, Key, Str, press
from talon import app, clip, ui
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string
from ..utils import surround, parse_words, parse_word, sentence_text, text, word
from talon.engine import engine


def engine_update(j):
    engine.cmd("g.update", name="dragon", enabled=False)


engine.register("ready", engine_update)


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
    "utils",
]

keymap = {}
keymap.update(
    {
        "dragon words": "<dgnwords>",
        "dragon dictation": "<dgndictation>",
        "slap": [Key("cmd-right enter")],
        "cd": "cd ",
        "cd talon home": "cd {}\n".format(TALON_HOME),
        "cd talon user": "cd {}\n".format(TALON_USER),
        "cd talon [user] emily": "cd {}/emily\n".format(TALON_USER),
        "cd talon plugins": "cd {}\n".format(TALON_PLUGINS),
        "talon logs": "cd {} && tail -f talon.log\n".format(TALON_HOME),
        "grep": "grep ",
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
        "[inside] (index | array)": ["[]", Key("left")],
        "block": ["{}", Key("left enter enter up tab")],
        "empty array": "[]",
        "comment see": "// ",
        "word queue": "queue",
        "word eye": "eye",
        "word bson": "bson",
        "word iter": "iter",
        "word no": "NULL",
        "word cmd": "cmd",
        "word dup": "dup",
        "word streak": ["streq()", Key("left")],
        "word printf": "printf",
        "word shell": "shell",
        "word Point2d": "Point2d",
        "word Point3d": "Point3d",
        "title Point": "Point",
        "word angle": "angle",
        "dunder in it": "__init__",
        "self taught": "self.",
        "(dickt in it | inside bracket | in bracket)": ["{}", Key("left")],
        "(in | inside) percent": ["%%", Key("left")],
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
        "funny": "ha ha",
        "menubar": Key("ctrl-f2"),
        "status menu": Key("ctrl-f8"),
        "my doc": Key("ctrl-f3"),
       }
)

ctx.keymap(keymap)
