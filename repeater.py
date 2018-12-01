from talon.voice import Context, Rep

ctx = Context("repeater")

def ordinal(n):
    '''
    Convert an integer into its ordinal representation::
        ordinal(0)   => '0th'
        ordinal(3)   => '3rd'
        ordinal(122) => '122nd'
        ordinal(213) => '213th'
    '''
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

keymap = {}

for n in range(2,100):
    keymap[ordinal(n)] = Rep(n-1)

ctx.keymap(keymap)
