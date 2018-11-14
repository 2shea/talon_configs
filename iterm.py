from talon.voice import Key, Context

ctx = Context('iterm', bundle='com.googlecode.iterm2')

keymap = {
    'preferences': Key('cmd-,'),
    '[toggle] full-screen': Key('cmd-shift-enter'),
    'exit session': [Key('ctrl-c'), 'exit\n'],
    'broadcaster': Key('cmd-alt-i'),
    'clear session': [Key('ctrl-c'), 'clear\n'],
    'clean': Key('cmd-k'),
    'split horizontal': Key('cmd-shift-d'),
    'split vertical': Key('cmd-d'),
    'next (split | pane)': Key('cmd-]'),
    'last (split | pane)': Key('cmd-['),
    'move tab left': Key('shift-cmd-left'),
    'move tab right': Key('shift-cmd-right'),
    '(subble | subtle)': 'subl ',
    '(scratch | scrap)': Key('ctrl-u'),
    'find': Key('cmd-f'),
    'jump back': Key('ctrl-[ b'),
    'jump [forward]': Key('ctrl-] f'),
}

ctx.keymap(keymap)
