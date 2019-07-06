from talon.voice import Str
from .bundle_groups import FILETYPE_SENSITIVE_BUNDLES

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
    "talent": "talon",
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


number_conversions = {"oh": "0"}  # 'oh' => zero
for i, w in enumerate(
    ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
):
    number_conversions[str(i)] = str(i)
    number_conversions[w] = str(i)
    number_conversions["%s\\number" % (w)] = str(i)


def parse_words_as_integer(words):
    # TODO: Once implemented, use number input value rather than manually
    # parsing number words with this function

    # Ignore any potential non-number words
    number_words = [w for w in words if str(w) in number_conversions]

    # Somehow, no numbers were detected
    if len(number_words) == 0:
        return None

    # Map number words to simple number values
    number_values = list(map(lambda w: number_conversions[w.word], number_words))

    # Filter out initial zero values
    normalized_number_values = []
    non_zero_found = False
    for n in number_values:
        if not non_zero_found and n == "0":
            continue
        non_zero_found = True
        normalized_number_values.append(n)

    # If the entire sequence was zeros, return single zero
    if len(normalized_number_values) == 0:
        normalized_number_values = ["0"]

    # Create merged number string and convert to int
    return int("".join(normalized_number_values))


def is_in_bundles(bundles):
    return lambda app, win: any(b in app.bundle for b in bundles)


def is_filetype(extensions=()):
    def matcher(app, win):
        if is_in_bundles(FILETYPE_SENSITIVE_BUNDLES)(app, win):
            if any(ext in win.title for ext in extensions):
                return True
            else:
                return False
        return True

    return matcher
