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
        "next slide": [Key("pgdown")],
        "last slide": [Key("pgup")],
        "home slide": [Key("home")],
        "present": [Key("f10")],
        "present fullscreen": [Key("f9")],
        "present clone": [Key("f7")],
        "restart timer": [Key("f8")],
        "video play": [
            Key("tab"),
            Key("tab"),
            Key("tab"),
            Key("tab"),
            Key("tab"),
            Key("enter"),
            Key("shift-tab"),
            Key("shift-tab"),
            Key("shift-tab"),
            Key("enter"),
        ],
        "video finish": [
            Key("tab"),
            Key("tab"),
            Key("tab"),
            Key("enter"),
            Key("tab"),
            Key("tab"),
            Key("tab"),
        ],
    }
)
sleep_group.load()
