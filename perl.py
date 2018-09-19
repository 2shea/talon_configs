from talon.voice import Context, Key

def perl(app, win):
    return (any(win.doc.endswith(x) for x in ('.pm','.pl','.PM','.t','.tt')) or win.app.name == 'iTerm2' )

ctx = Context('perl', func=perl)

ctx.keymap({
	'pearl': 'perl',
    'on (deaf | dev | deft)': 'undef',
    'log for pearl': 'Log4perl',
    'see pan (m | em | minus)': 'cpanm ',
    'pearl tidy': 'perltidy',
    '(warren | worn | warn)': 'warn',
    '(die ag | diag)': 'diag',
    'paramus': 'params',
})

