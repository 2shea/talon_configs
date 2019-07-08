import random
from talon.voice import Context, press
from talon import clip
from .utils import extract_word
from .picker import selection_picker
from ..emoji_data_python import emoji_data as emojis, emoji_short_names as emoji_names

context = Context("emojis")

def emoji_helper(emoji):
	# TODO: preserve clipboard
	clip.set(emoji)
	press("cmd-v", wait=2000)

def random_emoji():
    emoji = random.choice(emojis)
    emoji_helper(emoji.char)

def search(m):
	name = extract_word(m)
	emojis = set([emoji_names[key].char for key in emoji_names.keys() if name in key])
	selection_picker(title="Emojis", template="picker.html", data=emojis)

context.keymap({
    "emoji random": lambda _: random_emoji(),
	"emoji search <dgnwords>": search,
	"emoji raised [eyebrow]": lambda _: emoji_helper("🤨"),
	"emoji monocle": lambda _: emoji_helper("🧐"),
	"emoji whale": lambda _: emoji_helper("🐋"),
	"emoji snail": lambda _: emoji_helper("🐌"),
	"emoji thumbs [up]": lambda _: emoji_helper("👍"),
})
