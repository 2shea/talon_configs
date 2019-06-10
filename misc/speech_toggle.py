from talon.voice import Context, ContextGroup, Key
from talon.engine import engine
from talon_plugins import speech

sleep_group = ContextGroup("sleepy")
sleepy = Context("sleepy", group=sleep_group)

sleepy.keymap(
    {
        "talon sleep": lambda m: speech.set_enabled(False),
        "talon wake": lambda m: speech.set_enabled(True),
        "dragon mode": [
            lambda m: speech.set_enabled(False),
            lambda m: engine.mimic("wake up".split()),
        ],
        "talon mode": [
            lambda m: speech.set_enabled(True),
            lambda m: engine.mimic("go to sleep".split()),
        ],
        "next slide": [Key("pgdown")],
        "last slide": [Key("pgup")],
        "home slide": [Key("home")],
        "present": [Key("f16")],
        "present fullscreen": [Key("f17")],
        "restart timer": [Key("f18")],
        "present help": [Key("f13")],
    }
)
sleep_group.load()
