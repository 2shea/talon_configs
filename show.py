import string
from talon import voice
from talon.voice import Context, Str
from talon import canvas
from talon import ui
from talon.skia import Rect

ctx = Context('show')
alphabet_context = Context('alphabet_context')

# font size of the overlay
font_size = 18
# left padding of the font in the overlay
padding_left = 20

def draw_alphabet(canvas):
	paint = canvas.paint
	paint.textsize = font_size
	paint.color = '000000'
	paint.style = paint.Style.FILL
	canvas.draw_rect(Rect(canvas.x, canvas.y, canvas.width, canvas.height))

	line_height = paint.get_fontmetrics(1.5)[0]

	paint.color = 'ffffff'

	try:
		from user import std
		alnum = std.alpha_alt
	except:
		# TODO log an error
		alnum = []

	num = 1
	for k, v in zip(alnum, string.ascii_lowercase):
		canvas.draw_text('%s - %s' % (k,v), canvas.x + padding_left, canvas.y + (num * line_height))
		num += 1

# initialize the overlay
screen = ui.main_screen()
w, h = screen.width, screen.height

x_position = w / 3
y_position = h / 4
x_dimension = w / 3
y_dimension = h / 2

panel = canvas.Canvas(x_position, y_position, x_dimension, y_dimension)
panel.register('draw', draw_alphabet)
panel.hide()

def show_alphabet(_):
	global alphabet_context

	panel.show()
	panel.freeze()

	keymap = {
		'(0 | exit | escape)': lambda x: close_alphabet(),
	}

	alphabet_context.keymap(keymap)
	alphabet_context.load()

def close_alphabet():
    panel.hide()
    alphabet_context.unload()

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

keymap = {
	'show contexts': show_ctx,
	'show alphabet': show_alphabet,
	# ' context <dgndictation>': lambda m: show_context(m),
}

ctx.keymap(keymap)