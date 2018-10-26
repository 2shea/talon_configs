from talon.voice import Key, Context

ctx = Context('iterm', bundle='com.googlecode.iterm2')

keymap = {
    '[toggle] full-screen': Key('cmd-shift-enter'),
    'exit session': [Key('ctrl-c'), 'exit\n'],
    'broadcaster': Key('cmd-alt-i'),
    'clear session': [Key('ctrl-c'), 'clear\n'],
    'clean': Key('cmd-k'),
    'split horizontal': Key('cmd-shift-d'),
    'split vertical': Key('cmd-d'),
    'next (split | pane)': Key('cmd-]'),
    'last (split | pane)': Key('cmd-['),
    '(subble | subtle)': 'subl ',
    '(scratch | scrap)': Key('ctrl-u'),
    'find': Key('cmd-f'),
    'jump back': Key('ctrl-[ b'),
    'jump [forward]': Key('ctrl-] f'),
}

ctx.keymap(keymap)
