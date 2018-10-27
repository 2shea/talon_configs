from talon import app, clip, cron
from talon.engine import engine
from talon.voice import Word, Key, Context, Str, press
from talon.webview import Webview

from user.std import parse_word
import os

########################################################################
# global settings
########################################################################

# a list of homophones where each line is a comma separated list
# e.g. where,wear,ware
# a suitable one can be found here:
# https://github.com/pimentel/homophones
cwd = os.path.dirname(os.path.realpath(__file__))
homophones_file = os.path.join(cwd, 'homophones.csv')
# if quick_replace, then when a word is selected and only one homophone exists,
# replace it without bringing up the options
quick_replace = True
########################################################################

context = Context('homophones')
pick_context = Context('pick')

phones = {}
canonical = []
with open(homophones_file, 'r') as f:
    for h in f:
        h = h.rstrip()
        h = h.split(',')
        canonical.append(max(h, key=len))
        for w in h:
            w = w.lower()
            others = phones.get(w, None)
            if others is None:
                phones[w] = sorted(h)
            else:
                # if there are multiple hits, collapse them into one list
                others += h
                others = set(others)
                others = sorted(others)
                phones[w] = others

all_homophones = phones

active_word_list = None
# is_selection = False

webview = Webview()
template = '''
<style type="text/css">
body {
    padding: 0;
    margin: 0;
    font-size: 200%;
}
.contents {
    width: 100%;
}
td {
    text-align: left;
    margin: 0;
    padding: 0;
    padding-left: 10px;
}

table {
    counter-reset: rowNumber;
}

table tr {
    counter-increment: rowNumber;
}

table tr td:first-child::before {
    content: counter(rowNumber);
    min-with: 1em;
    margin-right: 0.5em;
}

</style>
<h3>homophones</h3>
<div class="contents">
<table>
{% for word in homophones %}
    <tr><td>{{ word }}</td></tr>
{% endfor %}
</table>
</div>
'''


def close_homophones():
    webview.hide()
    pick_context.unload()


def make_selection(m, is_selection, transform=lambda x: x):
    cron.after('0s', close_homophones)
    words = m._words
    d = None
    if len(words) == 1:
        d = int(parse_word(words[0]))
    else:
        d = int(parse_word(words[1]))
    w = active_word_list[d - 1]
    if len(words) > 1:
        w = transform(w)
    if is_selection:
        clip.set(w)
        press('cmd-v', wait=0)
    else:
        Str(w)(None)


def get_selection():
    with clip.capture() as s:
        press('cmd-c', wait=0)
    return s.get()


def raise_homophones(m, force_raise=False, is_selection=False):
    global pick_context
    global active_word_list

    if is_selection:
        word = get_selection()
        word = word.strip()
    # elif hasattr(m, 'dgndictation'):
        # this mode is currently disabled...
        # experimenting with using a canonical representation and not using
        # dgndictation
        # word = str(m.dgndictation[0]._words[0])
        # word = parse_word(word)
    elif len(m._words) >= 2:
        word = str(m._words[len(m._words) - 1])
        word = parse_word(word)

    word = word.lower()

    if word not in all_homophones:
        app.notify('homophones.py', '"%s" not in homophones list' % word)
        return

    active_word_list = all_homophones[word]
    if (
        is_selection
        and len(active_word_list) == 2
        and quick_replace
        and not force_raise
    ):
        if word == active_word_list[0].lower():
            new = active_word_list[1]
        else:
            new = active_word_list[0]
        clip.set(new)
        press("cmd-v", wait=0)
        return

    valid_indices = range(len(active_word_list))

    webview.render(template, homophones=active_word_list)
    webview.show()

    keymap = {
        'pick 0': lambda x: close_homophones(),
    }

    def capitalize(x):
        return x[0].upper() + x[1:]

    def uppercase(x):
        return x.upper()

    def lowercase(x):
        return x.lower()

    keymap.update({'pick %s' % (i + 1):
                   lambda m: make_selection(m, is_selection)
                   for i in valid_indices})
    keymap.update({'(title | capitalize | ship) %s' % (i + 1):
                   lambda m: make_selection(m, is_selection, capitalize)
                   for i in valid_indices})
    keymap.update({'(upper | uppercase | yeller) %s' % (i + 1):
                   lambda m: make_selection(m, is_selection, uppercase)
                   for i in valid_indices})
    keymap.update({'(lower | lowercase) %s' % (i + 1):
                   lambda m: make_selection(m, is_selection, lowercase)
                   for i in valid_indices})
    pick_context.keymap(keymap)
    pick_context.load()


# keymap = {
#     # Usage:
#     # 'homophones word' to look up those homophones.
#     # when the list pops up, say appropriate number or zero
#     # (leave and do nothing).
#     # can also call 'homophones' without any arguments.
#     # it will look at the selected text and look that up.
#     # 'phones [<dgndictation>]': raise_homophones,
#     # 'force phones [<dgndictation>]': lambda m: raise_homophones(m, True),
# }

context.keymap({
    'phones {homophones.all}': raise_homophones,
    'phones': lambda m: raise_homophones(m, is_selection=True),
    'force phones {homophones.canonical}': lambda m: raise_homophones(m, force_raise=True),
    'force phones': lambda m: raise_homophones(m, force_raise=True, is_selection=True),
})
context.set_list('all', all_homophones.keys())
