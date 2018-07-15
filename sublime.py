from talon.voice import Key, press, Str, Context

ctx = Context('sublime', bundle='com.sublimetext.3')

############## support for parsing numbers as command postfix

numeral_map = dict((str(n), n) for n in range(0, 20))
for n in [20, 30, 40, 50, 60, 70, 80, 90]:
    numeral_map[str(n)] = n
numeral_map["oh"] = 0 # synonym for zero

numerals          = ' (' + ' | '.join(sorted(numeral_map.keys())) + ')+'
optional_numerals = ' (' + ' | '.join(sorted(numeral_map.keys())) + ')*'

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


def parse_word(word):
    word = str(word).lstrip('\\').split('\\', 1)[0]
    return word


######### actions and helper functions
def jump_to_bol(m):
    line = text_to_number(m)
    press('ctrl-g')
    Str(str(line))(None)
    press('enter')

def jump_to_end_of_line():
    press('cmd-right')

def jump_to_beginning_of_text():
    press('cmd-left')

def jump_to_nearly_end_of_line():
    press('left')

def jump_to_bol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        else:
            press('ctrl-a')
            press('cmd-left')
        then()
    return fn

def jump_to_eol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        press('cmd-right')
        then()
    return fn


def toggle_comments(*unneeded):
   press('cmd-/')

def snipline():
    press('ctrl-shift-k')

def get_first_word(m):
    return str(m.dgndictation[0]._words[0])

def execute_atom_command(command, parameters=None):
    press(atom_hotkey)
    press(command)
    if parameters:
        Str(parameters)(None)
        press('enter')

def find_next(m):
    execute_atom_command(COMMANDS.FIND_NEXT, get_first_word(m))

def find_previous(m):
    execute_atom_command(COMMANDS.FIND_PREVIOUS, get_first_word(m))

def copy_line(m):
    line = text_to_number(m)
    execute_atom_command(COMMANDS.COPY_LINE, str(line))

def move_line(m):
    line = text_to_number(m)
    execute_atom_command(COMMANDS.MOVE_LINE, str(line))

def select_lines(m):
    # NB: line_range is e.g. 99102, which is parsed in
    #  the atom package as lines 99..102
    line_range = text_to_number(m)
    execute_atom_command(COMMANDS.SELECT_LINES, str(line_range))

keymap = {
    # 'sprinkle' + optional_numerals: jump_to_bol,
    'spring' + optional_numerals: jump_to_eol_and(jump_to_beginning_of_text),
    # 'sprinkler'
    # 'dear' + optional_numerals: jump_to_eol_and(lambda: None),
    'smear' + optional_numerals: jump_to_eol_and(jump_to_nearly_end_of_line),
    'trundle': toggle_comments,
    'trundle super': Key('cmd-alt-/'),
    'trundle' + numerals: jump_to_bol_and(toggle_comments),
    'jolt': Key('cmd-shift-d'),

    'snipline' + optional_numerals: jump_to_bol_and(snipline),
    'snipline super': Key('ctrl-shift-k'),

    # 'snipple': [Key(atom_hotkey), Key(COMMANDS.DELETE_TO_BOL)],
    # 'snipper': [Key(atom_hotkey), Key(COMMANDS.DELETE_TO_EOL)],

    'bracken': [Key('ctrl-shift-m')],

    'copy line' + numerals: copy_line,
    'move line' + numerals: move_line,

    'crew <dgndictation>': find_next,
    'trail <dgndictation>': find_previous,

    'tools beautify': Key('ctrl-alt-f'),

    'shackle': Key('cmd-l'),
    'select range' + numerals: select_lines,

    # 'shockey': Key('cmd-shift-enter'),
    # 'shockoon': Key('cmd-right enter'),
    # 'sprinkoon' + numerals: jump_to_eol_and(lambda: press('enter')),

    'go line': Key("ctrl-g"),
    'tab last': Key('cmd-shift-['),
    'tab next': Key('cmd-shift-]'),
}

ctx.keymap(keymap)

