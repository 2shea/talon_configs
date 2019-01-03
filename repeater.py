from talon.voice import Context, Rep

ctx = Context("repeater")

ordinals = {}

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

for n in range(2,100):
    ordinals[ordinal(n)] = n-1

ctx.set_list('ordinals', ordinals.keys())


def r(n):
    return lambda _: Rep(n)

def repeat(m):
    print(m['repeater.ordinals'][0])
    o = m['repeater.ordinals'][0]
    print(ordinals[o])
    return r(o)

ctx.keymap({
    '{repeater.ordinals}': repeat,
})
