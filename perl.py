from talon.voice import Context, Key


def perl(app, win):
    return (
        any(win.doc.endswith(x) for x in (".pm", ".pl", ".PM", ".t", ".tt", ".py"))
        or win.app.name == "iTerm2"
    )

# ctx = Context("perl", func=perl)
ctx = Context("perl")

ctx.vocab = ["params", "perltidy", "githook", "undef", "perl", "diag", "plack", "rehash"]

ctx.keymap(
    {
        "log for pearl": "Log4perl",
        "perl env": "plenv ",
        "see pan (m | em | minus)": "cpanm ",
        "(warren | worn | warn)": "warn ",
        "use pragmas": "use strict;\nuse warnings;\n",
        "use dumper": "use Data::Dumper;",
        "perl use": "use ",
        "perl require": "require ",
        "perl local": "local ",
        "perl my": "my ",
        "perl keys": "keys ",
        "perl scalar": "scalar ",
        "perl sub": "sub ",
        "perl like": "like ",
        "perl (exists | exist)": "exists ",
        "perl (defined | define)": "defined ",
        "perl defined or": "//",
        "op [perl] defined or": " // ",
        "perl [auto] increment": "++",
        "perl [auto] decrement": "--",
        "perl match": "=~",
        "op [perl] match": " =~ ",
        "perl (no | negated) match": "!~",
        "op [perl] (no | negated) match": " !~ ",
        "perl (equals | eek)": " eq ",
        "perl not (equals | eek)": " ne ",
        "[op] perl compare": " cmp ",
        "perl (lowercase | lower)": "lc ",
        "perl (uppercase | upcase | upper)": "uc ",
        "perl map": "map ",
        "perl (exclusive | ex) or": " xor ",
        "op [perl] (diamond | input)": ["<>", Key("left")],
    }
)
