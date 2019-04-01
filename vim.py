from talon.voice import Key, press, Str, Context

ctx = Context("vim")

ctx.keymap({
	"vim save quit": Key("esc : w q enter"),
	"vim save": Key("esc : w enter"),
	"vim quit": Key("esc : q"),
	"vim quit bang": Key("esc : q !"),
})
