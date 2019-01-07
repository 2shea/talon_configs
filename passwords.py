from talon import keychain
from talon.voice import Context, Key, Str

# using the repl, you can run `keychain.add('steam', 'my-username', 'my-password')`
# ~/.talon/bin/repl is a command you can run
# then when you say `password steam` it will pull it out of the OS keychain and type it
# the autofill thing is just invoking 1password
# the someservice example is a service where the username and the service name are the same
# e.g. `keychain.add('someservice', 'someservice', 'password')`

def insert(service, user=None):
    if user is None:
        user = service
    def wrapper(m):
        pw = keychain.find(service, user)
        Str(pw)(None)
    return wrapper

ctx = Context('keychain')
ctx.keymap({
    # 'password steam': insert('steam', 'my-username'),
    # 'password someservice': insert('someservice'),
    # 'password auto fill': Key('cmd-\\'),
})