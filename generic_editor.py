from talon.voice import Key, press, Str, Context
from .utils import parse_word

ctx = Context("generic_editor")

############## support for parsing numbers as command postfix

numeral_map = dict((str(n), n) for n in range(0, 20))
for n in [20, 30, 40, 50, 60, 70, 80, 90]:
    numeral_map[str(n)] = n
numeral_map["oh"] = 0  # synonym for zero

numerals = " (" + " | ".join(sorted(numeral_map.keys())) + ")+"
optional_numerals = " (" + " | ".join(sorted(numeral_map.keys())) + ")*"


def text_to_number(m):

    tmp = [str(s).lower() for s in m._words]
    words = [parse_word(word) for word in tmp]

    result = 0
    factor = 1
    for word in reversed(words):
        if word not in numerals:
            # we consumed all the numbers and only the command name is left.
            break

        result = result + factor * int(numeral_map[word])
        factor = 10 * factor

    return result


######### actions and helper functions
def jump_to_bol(m):
    line = text_to_number(m)
    press("ctrl-g")
    Str(str(line))(None)
    press("enter")


def jump_to_end_of_line():
    press("cmd-right")


def jump_to_beginning_of_text():
    press("cmd-left")


def jump_to_nearly_end_of_line():
    press("left")


def jump_to_bol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        else:
            press("ctrl-a")
            press("cmd-left")
        then()

    return fn


def jump_to_eol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        press("cmd-right")
        then()

    return fn


def toggle_comments(*unneeded):
    press("cmd-/")


def snipline():
    press("ctrl-shift-k")


def get_first_word(m):
    return str(m.dgndictation[0]._words[0])


keymap = {
	"(trundle | comment)": toggle_comments,
	"(trundle | comment)"
	+ numerals: jump_to_bol_and(toggle_comments),  # noop for plain/text
	"snipline" + optional_numerals: jump_to_bol_and(snipline),
	"sprinkle" + optional_numerals: jump_to_bol,
	"spring" + optional_numerals: jump_to_eol_and(jump_to_beginning_of_text),
	"sprinkoon" + numerals: jump_to_eol_and(lambda: press("enter")),
	"dear" + optional_numerals: jump_to_eol_and(lambda: None),
	"smear" + optional_numerals: jump_to_eol_and(jump_to_nearly_end_of_line),

	# general
	"fullscreen": Key("ctrl-cmd-f"),

	# file
	"new": Key("cmd-n"),
	"(save | safe)": Key("cmd-s"),
	"close (file | tab)": Key("cmd-w"),

	# selection
	"(select | cell) up": Key("shift-up"),
	"(select | cell) down": Key("shift-down"),
	"(select | cell) all": Key("cmd-a"),
	"(select | cell) bottom ": Key("cmd-shift-down"),
	"(select | cell) right": Key("shift-right"),
	"(select | cell) left": Key("shift-left"),
	"(select | cell) (end | push)": Key("cmd-shift-right"),
	"(select | cell) (start | begin | pop)": Key("cmd-shift-left"),

	# edit
	"paste match": Key("cmd-shift-v"),
	"shove": Key("cmd-]"),
	"tug": Key("cmd-["),
	"(scrap | scratch | delete) word": Key("alt-backspace"),
	"(scrap | scratch | delete) (begin | start)": Key("cmd-backspace"),

	# navigation
	"push": Key("cmd-right"),
	"pop": Key("cmd-left"),
}

ctx.keymap(keymap)

