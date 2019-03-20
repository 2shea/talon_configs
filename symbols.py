from talon.voice import Context

context = Context("symbols")

context.keymap(
    {
        "question [mark]": "?",
        "tilde": "~",
        "(bang | exclamation point)": "!",
        "dollar [sign]": "$",
        "(downscore | underscore)": "_",
        "colon": ":",
        "(paren | left paren)": "(",
        "(rparen | are paren | right paren)": ")",
        "(bracket | brack | left bracket)": "{",
        "(rbrack | are bracket | right bracket)": "}",
        "(angle | left angle | less than)": "<",
        "(rangle | are angle | right angle | greater than)": ">",
        "(star | asterisk)": "*",
        "(pound | hash [sign] | octo | thorpe | number sign)": "#",
        "percent [sign]": "%",
        "caret": "^",
        "at sign": "@",
        "(and sign | ampersand )": "&",
        "pipe": "|",
        "(dubquote | double quote)": '"',
        "triple quote": "'''",
        "(dot dot | dotdot)": "..",
        "comma and": ", ",
        "plus": "+",
        "arrow": "->",
        "dub arrow": "=>",
        "op dub": " => ",
        "(op | pad) colon": " : ",
        "indirect": "&",
        "dereference": "*",
        "(op equals | assign)": " = ",
        "op (minus | subtract | sub)": " - ",
        "op (plus | add)": " + ",
        "op (times | multiply)": " * ",
        "op divide": " / ",
        "op mod": " % ",
        "[op] (minus | subtract | sub) equals": " -= ",
        "[op] (plus | add) equals": " += ",
        "[op] (times | multiply) equals": " *= ",
        "[op] divide equals": " /= ",
        "[op] mod equals": " %= ",
        "(op | is) greater [than]": " > ",
        "(op | is) less [than]": " < ",
        "(op | is) equal": " == ",
        "(op | is) not equal": " != ",
        "(op | is) greater [than] or equal": " >= ",
        "(op | is) less [than] or equal": " <= ",
        "(op (power | exponent) | to the power [of])": " ** ",
        "op and": " && ",
        "op or": " || ",
        "[op] (logical | bitwise) and": " & ",
        "[op] (logical | bitwise) or": " | ",
        "(op | logical | bitwise) (ex | exclusive) or": " ^ ",
        "[(op | logical | bitwise)] (left shift | shift left)": " << ",
        "[(op | logical | bitwise)] (right shift | shift right)": " >> ",
        "(op | logical | bitwise) and equals": " &= ",
        "(op | logical | bitwise) or equals": " |= ",
        "(op | logical | bitwise) (ex | exclusive) or equals": " ^= ",
        "[(op | logical | bitwise)] (left shift | shift left) equals": " <<= ",
        "[(op | logical | bitwise)] (right shift | shift right) equals": " >>= ",
    }
)
