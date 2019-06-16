from talon.voice import Context, press
from talon import clip

context = Context("emoji")


def emoji_helper(emoji):
    clip.set(emoji)
    press("cmd-v", wait=0)


context.keymap(
    {
        "emoji raised": lambda m: emoji_helper("🤨"),
        "emoji monocle": lambda m: emoji_helper("🧐"),
        "emoji whale": lambda m: emoji_helper("🐋"),
        "emoji snail": lambda m: emoji_helper("🐌"),
        "emoji thumbs up": lambda m: emoji_helper("👍"),
    }
)
