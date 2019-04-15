from talon.voice import Context, Key

context = Context("1password")

context.keymap(
	{
		"password fill": Key("cmd-\\"),
		"password show": Key("opt-cmd-\\"),
	}
)