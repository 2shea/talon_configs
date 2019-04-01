from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ui

apps = {}

overrides = {"from": "Google Chrome"}


def switch_app(m):
    name = str(m._words[1])

    full = apps.get(name)
    if not full:
        return
    for app in ui.apps():
        if app.name == full:
            app.focus()
            break


ctx = Context("switcher")
keymap = {"(focus | folk) {switcher.apps}": switch_app}
ctx.keymap(keymap)


def update_lists():
    global apps
    new = {}
    for app in ui.apps():
        words = app.name.split(" ")
        for word in words:
            if word and not word in new:
                new[word] = app.name
        new[app.name] = app.name
    for override in overrides:
        new[override] = overrides[override]
    if set(new.keys()) == set(apps.keys()):
        return
    ctx.set_list("apps", new.keys())
    apps = new


def ui_event(event, arg):
    if event in ("app_activate", "app_deactivate", "app_launch", "app_close"):
        update_lists()


ui.register("", ui_event)
update_lists()
