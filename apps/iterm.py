from talon.voice import Key, Context

ctx = Context("iterm", bundle="com.googlecode.iterm2")

keymap = {
    "preferences": Key("cmd-,"),
    "[toggle] full-screen": Key("cmd-shift-enter"),
    "exit session": [Key("ctrl-c"), "exit\n"],
    "broadcaster": Key("cmd-alt-i"),
    "clear session": [Key("ctrl-c"), "clear\n"],
    "clean": Key("cmd-k"),
    "split horizontal": Key("cmd-shift-d"),
    "split vertical": Key("cmd-d"),
    "next (split | pane)": Key("cmd-]"),
    "last (split | pane)": Key("cmd-["),
    "max (split | pane)": Key("shift-cmd-enter"),
    "move tab left": Key("shift-cmd-left"),
    "move tab right": Key("shift-cmd-right"),
    "(subble | subtle)": "subl ",
    "(scratch | scrap)": Key("ctrl-u"),
    "(shell | i term )search": Key("cmd-f"),
    "jump back": Key("ctrl-[ b"),
    "jump [forward]": Key("ctrl-] f"),
    "rerun": [Key("up"), Key("enter")],
    "sky": Key("cmd-ctrl-pageup"),
    "floor": Key("cmd-ctrl-pagedown"),
    "paste history": Key("shift-cmd-h"),

    # these require some changes to preferences:
    # https://coderwall.com/p/h6yfda/use-and-to-jump-forwards-backwards-words-in-iterm-2-on-os-x
    "(shall | shell) (stone | jack)": Key("alt-b"),
    "(shall | shell) (step | jump)": Key("alt-f"),
}

ctx.keymap(keymap)
