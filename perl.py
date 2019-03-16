from talon.voice import Context, Key


def perl(app, win):
    return (
        any(win.doc.endswith(x) for x in (".pm", ".pl", ".PM", ".t", ".tt"))
        or win.app.name == "iTerm2"
    )


ctx = Context("perl", func=perl)

ctx.vocab = ["params", "perltidy", "githook", "undef", "perl", "diag", "plack", "rehash"]

ctx.keymap(
    {
        "log for pearl": "Log4perl",
        "perl env": "plenv ",
        "see pan (m | em | minus)": "cpanm ",
        "(warren | worn | warn)": "warn ",
        "use pragmas": "use strict;\nuse warnings;\n",
        "use dumper": "use Data::Dumper;",
    }
)
