import random
from talon.voice import Context, press
from talon import clip
from ..emoji_data_python import emoji_data as emojis

context = Context("emojis")


def random_emoji():
    emoji = random.choice(emojis)
    # TODO: preserve clipboard
    clip.set(emoji.char)
    press("cmd-v", wait=2000)


context.keymap({
    "emoji random": lambda _: random_emoji()
})
