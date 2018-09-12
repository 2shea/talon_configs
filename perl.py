from talon.voice import Context, Key

def perl(app, win):
    print(('win.doc', win.doc))
    print(('win.title', win.title))
    return any(win.doc.endswith(x) for x in ('.pm','.pl','.PM','.t'))
    # return win.doc.endswith('.pl')

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

