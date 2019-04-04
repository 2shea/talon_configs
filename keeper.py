from talon.voice import Context, engine, Str

ctx = Context("keeper")


def keeper(j):
    if j["cmd"] == "p.end" and j["grammar"] == "talon":
        phrase = j["phrase"]
        if phrase and phrase[0] == "keeper":
            # Str(' '.join(map(parse_word, phrase[1:])))(None)
            Str(" ".join(phrase[1:]))(None)
            j["cmd"] = "p.skip"


engine.register("pre:phrase", keeper)
ctx.keymap({"keeper [<dgndictation>]": lambda m: None})
