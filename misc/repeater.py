"""
This module contains generic repeat commands that can be used following any
other command, e.g. "go down" or "delete" x many times. The repeat commands are
the ordinal representation of the total number of times to execute the
command, so "go down 4th" will go down 4 times.

A few reasons to use ordinals:
- Regular numbers are already heavily used
- Made up words are difficult to learn and remember
- Ordinals don't need to be memorized
- Ordinals are not likely to collide with other commands
"""
from talon.voice import Context, Rep, talon

ctx = Context("repeater")

ordinals = {}


def ordinal(n):
    """
    Convert an integer into its ordinal representation::
        ordinal(0)   => '0th'
        ordinal(3)   => '3rd'
        ordinal(122) => '122nd'
        ordinal(213) => '213th'
    """
    n = int(n)
    suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    return str(n) + suffix


for n in range(2, 100):
    ordinals[ordinal(n)] = n - 1

ctx.set_list("ordinals", ordinals.keys())


def repeat(m):
    o = m["repeater.ordinals"][0]
    repeater = Rep(int(ordinals[o]))
    repeater.ctx = talon
    return repeater(None)


ctx.keymap({"{repeater.ordinals}": repeat})
