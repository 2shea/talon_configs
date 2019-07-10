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
        "talon demo": [
            lambda m: speech.set_enabled(True),
            lambda m: engine.mimic("go to sleep".split()),
            Key("tab"),
        ],
        "(next slide | go next)": [Key("pgdown")],
        "last slide": [Key("pgup")],
        "beginning slide": [Key("home")],
        "present notes": [Key("f10")],
        "present (fullscreen | full)": [Key("f9")],
        "present clone": [Key("f7")],
        "restart timer": [Key("f8")],
        "video play": [Key("tab"), Key("space")],
        "video (fullscreen | full)": Key("ctrl-enter"),
    }
)
sleep_group.load()
