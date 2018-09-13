from talon.voice import Context, Key

def perl(app, win):
    # print(('win.doc', win.doc))
    # print(('win.title', win.title))
    # print(('win.app', win.app.name))
    return (any(win.doc.endswith(x) for x in ('.pm','.pl','.PM','.t')) or win.app.name == 'iTerm2' )

ctx = Context('perl', func=perl)

ctx.keymap({
	'pearl': 'perl',
    'on (deaf | dev | deft)': 'undef',
    'die':'die',
    'self':'self',
    'class':'class',
    'return': 'return',
    'package': 'package',
    'use': 'use',
    'strict': 'strict',
    'log for pearl': 'Log4perl',


})

