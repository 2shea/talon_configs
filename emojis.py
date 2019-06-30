import random
from talon.voice import Context, press
from talon import clip
from .utils import get_word
from ..emoji_data import emojis, emoji_names

context = Context("emojis")


def random_emoji():
    emoji = random.choice(emojis)
    # TODO: preserve clipboard
    clip.set(emoji.char)
    press("cmd-v", wait=2000)


def find_emoji(m):
    name = get_word(m)
    emojis = list(set([emoji_names[key] for key in emoji_names.keys() if name in key]))
    clip.set("".join([e.char for e in emojis]))
    press("cmd-v", wait=2000)


context.keymap(
    {"emoji random": lambda _: random_emoji(), "emoji search <dgnwords>": find_emoji}
)
