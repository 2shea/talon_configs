from talon.voice import Context, Key

ctx = Context("go")

ctx.vocab = [
    "golang",
    "func",
]


ctx.keymap(
    {
        "go format": "gofmt",
        "go var": "var ",
        "go error": "err",
        "go [short] assign": " := ",

    }
)
