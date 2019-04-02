from talon.voice import Key, press, Str, Context

ctx = Context("sublime", bundle="com.sublimetext.3")

keymap = {
    "(trundle | comment) super": Key("cmd-alt-/"),
    # general
    "sidebar": [Key("cmd-k"), Key("cmd-b")],
    "console": Key("ctrl-`"),
    "[command] pallet": Key("cmd-shift-p"),
    "column one": Key("alt-cmd-1"),
    "column two": Key("alt-cmd-2"),
    "column three": Key("alt-cmd-3"),
    # window
    "(subl | sublime) new window": Key("shift-cmd-n"),
    # close window
    # file
    "(save | safe) all": Key("cmd-alt-s"),
    "revert": Key("ctrl-alt-r"),  # requires adding key binding
    "go file": Key("cmd-t"),
    # selection
    "(select line | shackle)": Key("cmd-l"),
    "(select | cell) word": Key("cmd-d"),
    "all word": Key("cmd-ctrl-g"),  # expand currently selected word to all occurances
    "(select | cell) current": Key("ctrl-cmd-g"),  # select all occurrences of current selection
    "(select | cell) scope": Key("shift-cmd-space"),
    "(select | cell) (bracket | paren)": Key("ctrl-shift-m"),
    "bracken": [Key("ctrl-shift-m")],
    "(select | cell) indent": Key("shift-cmd-j"),
    "cursor up": Key("ctrl-shift-up"),
    "cursor down": Key("ctrl-shift-down"),
    "cursor push": Key("cmd-shift-l"),
    "cursor pop": [Key("cmd-shift-l"), Key("cmd-left")],
    "(cursor | select) undo": Key("cmd-u"),
    "undo (select | cursor)": Key("cmd-u"),
    "(select | cell) sky": Key("ctrl-shift-up"),
    "bounce [right]": Key("ctrl-alt-shift-right"),
    "bound": Key("ctrl-alt-shift-left"),
    "bounce (left | back)": Key("ctrl-alt-shift-left"),
    # edit
    "snipline super": Key("ctrl-shift-k"),
    "dup line": Key("cmd-shift-d"),
    "up slap": Key("cmd-shift-enter"),
    "(scrap | scratch | delete) end": [Key("cmd-k"), Key("cmd-k")],
    "(uppercase | upcase)": [Key("cmd-k"), Key("cmd-u")],
    "(lower | lowercase | downcase)": [Key("cmd-k"), Key("cmd-l")],
    # navigation
    "go line": Key("ctrl-g"),
    "tab last": Key("cmd-shift-["),
    "tab next": Key("cmd-shift-]"),
    "jump paren": Key("ctrl-m"),
    "jump [forward]": Key("ctrl-alt-f"),
    "(jump back | jack | jazz)": Key("ctrl-alt-b"),
    "jump (up | start)": Key("cmd-up"),
    "jump (down | end)": Key("cmd-down"),
    # find & replace
    "find": Key("cmd-f"),
    "expression": Key("alt-cmd-r"),
    "case insensitive": Key("alt-cmd-c"),
    "whole word": Key("alt-cmd-w"),
}

ctx.keymap(keymap)
