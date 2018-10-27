import string
from talon.voice import Context
from talon.webview import Webview
from user import std

ctx = Context('show')
alphabet_context = Context('alphabet_context')

webview = Webview()
template = '''
<style type="text/css">
body {
    padding: 0;
    margin: 0;
}
.contents {
    width: 100%;
}
td {
    text-align: left;
    margin: 0;
    padding: 0;
    padding-left: 5px;
}
</style>
<h3>alphabet</h3>
<div class="contents">
<table>
{% for word, letter in alphabet %}
    <tr><td>{{ letter }}</td><td>{{ word }}</td></tr>
{% endfor %}
</table>
</div>
'''

def show_alphabet(_):
	global alphabet_context

	alphabet = list(zip(std.alpha_alt, string.ascii_lowercase))

	webview.render(template, alphabet=alphabet)
	webview.show()

	keymap = {
		'(0 | quit | exit | escape)': lambda x: close_alphabet(),
	}

	alphabet_context.keymap(keymap)
	alphabet_context.load()

def close_alphabet():
    webview.hide()
    alphabet_context.unload()

keymap = {
	'[show] alphabet': show_alphabet,
}

ctx.keymap(keymap)