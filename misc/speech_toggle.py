from talon.voice import Context, ContextGroup, Key
from talon.engine import engine
from talon_plugins import speech

from talon.canvas import Canvas

class Indicator:
    def __init__(self):
        self.canvas = Canvas(0, 0, 100, 100)
        self.color = 'green'

    def render(self, color, m=None):
        self.color = color
        self.canvas.register('draw', self.draw)
        self.canvas.show()

    def draw(self, canvas):
        paint = canvas.paint
        paint.color = self.color
        paint.style = paint.Style.FILL
        canvas.draw_circle(50, 50, 10)

indicator = Indicator()
indicator.render('green')

sleep_group = ContextGroup("sleepy")
sleepy = Context("sleepy", group=sleep_group)

sleepy.keymap(
    {
        "talon sleep": [
            lambda m: speech.set_enabled(False),
            lambda m: indicator.render('gray'),
        ],
        "talon wake": [
            lambda m: speech.set_enabled(True),
            lambda m: indicator.render('green'),
        ],
        "dragon mode": [
            lambda m: speech.set_enabled(False),
            lambda m: engine.mimic("wake up".split()),
            lambda m: indicator.render('blue')
        ],
        "talon mode": [
            lambda m: speech.set_enabled(True),
            lambda m: engine.mimic("go to sleep".split()),
            lambda m: indicator.render('green'),
        ],
        "talon demo": [
            lambda m: speech.set_enabled(True),
            lambda m: engine.mimic("go to sleep".split()),
            Key("tab"),
            lambda m: indicator.render('green'),
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
