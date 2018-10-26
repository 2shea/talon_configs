from talon.voice import Context, Key

def perl(app, win):
    return (any(win.doc.endswith(x) for x in ('.pm','.pl','.PM','.t','.tt')) or win.app.name == 'iTerm2' )

ctx = Context('perl', func=perl)

ctx.vocab = [
    'params',
    'perltidy',
    'undef',
    'perl',
    'diag',
    'plack',
]

ctx.keymap({
    'log for pearl': 'Log4perl',
    'see pan (m | em | minus)': 'cpanm ',
    '(warren | worn | warn)': 'warn',
    'use pragmas': 'use strict;\nuse warnings;\n',
})

