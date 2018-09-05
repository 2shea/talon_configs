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
    # 'sprinkler'
    # 'dear' + optional_numerals: jump_to_eol_and(lambda: None),
    'smear' + optional_numerals: jump_to_eol_and(jump_to_nearly_end_of_line),
    'trundle': toggle_comments,
    'trundle super': Key('cmd-alt-/'),
    'trundle' + numerals: jump_to_bol_and(toggle_comments), # noop for plain/text

    # 'snipple': [Key(atom_hotkey), Key(COMMANDS.DELETE_TO_BOL)],
    # 'snipper': [Key(atom_hotkey), Key(COMMANDS.DELETE_TO_EOL)],

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

    # general
    'sidebar': [Key('cmd-k'), Key('cmd-b')],
    'fullscreen': Key('ctrl-cmd-f'),
    'column one' : Key('alt-cmd-1'),
    'column two': Key('alt-cmd-2'),
    'column three': Key('alt-cmd-3'),

    # file
    '(save | safe)': Key('cmd-s'),
    'close file': Key('cmd-w'),

    # selection
    'select line': Key('cmd-l'),
    'select word': Key('cmd-d'),
    'select all': Key('cmd-a'),
    'select scope': Key('shift-cmd-'),
    'cursor up': Key('ctrl-shift-up'),
    'cursor down': Key('ctrl-shift-down'),
    'cursor undo': Key('cmd-u'),

    # edit
    'wipe start': [Key('cmd-shift-left'), Key('backspace')],
    'wipe end': [Key('cmd-shift-right'), Key('backspace')],
    'snipline' + optional_numerals: jump_to_bol_and(snipline),
    'snipline super': Key('ctrl-shift-k'),
    'dent': Key('cmd-]'),
    'no dent': Key('cmd-['),
    'dup line': Key('cmd-shift-d'),
    'bracken': [Key('ctrl-shift-m')],
    'newline up': Key('cmd-shift-enter'),
    'newline down': Key('cmd-enter'),
    'paste match': Key('cmd-shift-v'),

    # navigation
    'go line': Key("ctrl-g"),
    'spring' + optional_numerals: jump_to_eol_and(jump_to_beginning_of_text),
    'tab last': Key('cmd-shift-['),
    'tab next': Key('cmd-shift-]'),
    'wipe start': [Key('cmd-shift-left'), Key('backspace')],
    'wipe end': [Key('cmd-shift-right'), Key('backspace')],
    'paren jump': Key('ctrl-m'),

    # find & replace
    'find': Key('cmd-f'),
}

ctx.keymap(keymap)

