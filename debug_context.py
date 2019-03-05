from talon import ui, voice


def ui_event(event, arg):
    print("ui_event", event, ui.active_app(), voice.talon.active, arg)


ui.register("", ui_event)
