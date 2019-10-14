from talon.voice import Key, Context

ctx = Context("sound_source")


keymap = {
    "sound source": Key("alt-ctrl-cmd-shift-s"),
}

ctx.keymap(keymap)
