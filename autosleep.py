from talon.engine import engine


def on_status(topic, j):
    if j['cmd'] == 'mic' and j['status'] == 'on':
        print('mic turned on, mimic "go to sleep"')
        engine.mimic('go to sleep')


engine.register('status', on_status)
