from talon.voice import Context, Key

context = Context("1password")

context.keymap(
    {
        # Global
        "password fill": Key("cmd-\\"),
        "password show": Key("alt-cmd-\\"),
        # App
        "password new": Key("cmd-n"),
        "password dup": Key("cmd-d"),
        "password edit": Key("cmd-e"),
        "password delete": Key("cmd-delete"),
    }
)
