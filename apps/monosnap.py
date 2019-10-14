from talon.voice import Context, Key

context = Context("Mono")

keymap = {
    "mono video": Key("cmd-ctrl-0"),
    "mono (play | pause)": Key("cmd-ctrl-1"),
    "mono stop": Key("cmd-ctrl-2"),
}

context.keymap(keymap)
