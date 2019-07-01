import random
from talon.voice import Context, press
from talon import clip
from .utils import get_word
from .picker import selection_picker
from ..emoji_data_python import emoji_data as emojis, emoji_short_names as emoji_names

context = Context("emojis")


def random_emoji():
    emoji = random.choice(emojis)
    # TODO: preserve clipboard
    clip.set(emoji.char)
    press("cmd-v", wait=2000)


def find_emoji(m):
    name = get_word(m)
    emojis = set([emoji_names[key] for key in emoji_names.keys() if name in key])
    selection_picker(title="Emojis", data=[emoji.char for emoji in emojis])


context.keymap(
    {"emoji random": lambda _: random_emoji(), "emoji search <dgnwords>": find_emoji}
)
