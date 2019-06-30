from talon.voice import Str

# cleans up some Dragon output from <dgndictation>
mapping = {
    "semicolon": ";",
    "new-line": "\n",
    "new-paragraph": "\n\n",
    "furnish": "varnish",
    "pseudo-": "sudo",
    "apt get": "apt-get",
    "krohn": "cron",
    "standard out": "stdout",
    "standard in": "stdin",
    "standard error": "stderr",
    "keep": "key",
    "keeper": "key",
    "crum": "chrome",
    "crump": "chrome",
    "laugh": "waf",
    "pearl": "perl",
    "cash": "cache",
    "gage": "gauge",
    "scaler": "scalar",
    "warren": "warn",
    "worn": "warn",
    "carl": "curl",
    "bcl": "vcl",
    "tubal": "tuple",
    "vastly": "fastly",
}

# used for auto-spacing
punctuation = set(".,-!?")


def parse_word(word):
    word = str(word).lstrip("\\").split("\\", 1)[0]
    word = mapping.get(word.lower(), word)
    return word


def join_words(words, sep=" "):
    out = ""
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += word
    return out


def parse_words(m):
    return list(map(parse_word, m.dgndictation[0]._words))


def insert(s):
    Str(s)(None)


def text(m):
    insert(join_words(parse_words(m)).lower())


def sentence_text(m):
    text = join_words(parse_words(m)).lower()
    insert(text.capitalize())


def word(m):
    text = get_word(m)
    insert(text.lower())


def get_word(m):
    return join_words(list(map(parse_word, m.dgnwords[0]._words)))


def surround(by):
    def func(i, word, last):
        if i == 0:
            word = by + word
        if last:
            word += by
        return word

    return func
