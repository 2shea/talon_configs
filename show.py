import string
from talon import voice
from talon.voice import Context, Str

ctx = Context('show')


def show_ctx(word):
	ret = ""
	for name, ctx in voice.talon.subs.items():
		if ctx in voice.talon.active:
			ret += f'[{ctx.name}]\n'
		else:
			ret += f'[{ctx.name}] (inactive)\n'
		# for trigger in ctx.triggers:
		#     ret += f' - {trigger}'
		Str(ret)(None)

def show_alpha(_):
	try:
		from user import std
		alnum = std.alpha_alt
	except:
		# TODO log an error
		alnum = []
	ret = ""
	for k, v in zip(alnum, string.ascii_lowercase):
		ret += f'{k} - {v}\n'
	Str(ret)(None)

keymap = {
	'[ all ] contexts': show_ctx,
	'alphabet': show_alpha,
	# ' context <dgndictation>': lambda m: show_context(m),
}

ctx.keymap(keymap)