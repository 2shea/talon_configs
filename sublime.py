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

keymap = {
    'trundle': toggle_comments,
    'trundle super': Key('cmd-alt-/'),
    'trundle' + numerals: jump_to_bol_and(toggle_comments), # noop for plain/text

    'tools beautify': Key('ctrl-alt-f'),

    'shackle': Key('cmd-l'),

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
    'all word': Key('cmd-ctrl-g'), # expand currently selected word to all occurances
    'select all': Key('cmd-a'),
    'select scope': Key('shift-cmd-space'),
    'select bracket': Key('ctrl-shift-m'),
    'select indent': Key('shift-cmd-j'),
    'cursor up': Key('ctrl-shift-up'),
    'cursor down': Key('ctrl-shift-down'),
    '(cursor | select) undo': Key('cmd-u'),
    'undo (select | cursor)': Key('cmd-u'),
    'select up': Key('shift-up'),
    'select down': Key('shift-down'),
    'select right': Key('shift-right'),
    'select left': Key('shift-left'),

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
    'delete word': Key('alt-backspace'),

    # navigation
    'go line': Key("ctrl-g"),
    'sprinkle' + optional_numerals: jump_to_bol,
    'spring' + optional_numerals: jump_to_eol_and(jump_to_beginning_of_text),
    'tab last': Key('cmd-shift-['),
    'tab next': Key('cmd-shift-]'),
    'wipe start': [Key('cmd-shift-left'), Key('backspace')],
    'wipe end': [Key('cmd-shift-right'), Key('backspace')],
    'paren jump': Key('ctrl-m'),
    'dear' + optional_numerals: jump_to_eol_and(lambda: None),
    'smear' + optional_numerals: jump_to_eol_and(jump_to_nearly_end_of_line),

    # find & replace
    'find': Key('cmd-f'),
}

keymap.update({'select down %s' % k: [Key('shift-down')] * k for k in range(1,10)})
keymap.update({'select up %s' % k: [Key('shift-up')] * k for k in range(1,10)})
keymap.update({'select right %s' % k: [Key('shift-right')] * k for k in range(1,10)})
keymap.update({'select left %s' % k: [Key('shift-left')] * k for k in range(1,10)})
keymap.update({'cursor up %s' % k: [Key('ctrl-shift-up')] * k for k in range(1,10)})
keymap.update({'cursor down %s' % k: [Key('ctrl-shift-down')] * k for k in range(1,10)})
keymap.update({'select word %s' % k: [Key('cmd-d')] * k for k in range(1,10)})

ctx.keymap(keymap)
