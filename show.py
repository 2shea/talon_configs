import string
import talon
from pprint import pprint
from collections import OrderedDict
from talon import voice
from talon.voice import Context, Key
from talon.webview import Webview
from user import basic_keys

ctx = Context('show')
webview_context = Context('webview_context')

webview = Webview()
# TODO: use a master template
templates = {

'alpha': '''
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
,
'commands': '''
	<style type="text/css">
	body {
	    padding: 0;
	    margin: 0;
	    min-width: 800px;
	    font-size: 14px;
	    max-height: 200%;
	    overflow: auto;
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
	<h3>{{ context_name }} commands</h3>
	<div class="contents" overflow=scroll max-height=8px>
	<table>
	{% for trigger, mapped_to in mapping.items() %}
	    <tr><td>{{ trigger }}</td><td>{{ mapped_to }}</td></tr>
	{% endfor %}
	</table>
	</div>
	'''
,
'contexts': '''
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
	<h3>contexts</h3>
	<div class="contents">
	<table>
	{% for index, context in contexts.items() %}
	    <tr>
	    	<td>{{ index }}</td><td>{{ context.name }}</td>
	    	<td>{% if context in actives %}✅{% else %}❌{%endif %} </td>
	    </tr>
	{% endfor %}
	</table>
	</div>
	'''
}

def show_alphabet(_):
	alphabet = list(zip(basic_keys.alpha_alt, string.ascii_lowercase))

	webview_context.keymap({'(0 | quit | exit | escape)': lambda x: close_webview()})
	webview_context.load()

	webview.render(templates['alpha'], alphabet=alphabet)
	webview.show()

def close_webview():
    webview.hide()
    webview_context.unload()

# needed because of how closures work in Python
def create_context_mapping(context):
	return lambda _: show_commands(context)

def show_contexts(_):
	contexts = OrderedDict()

	keymap = {
		'(0 | quit | exit | escape)': lambda x: close_webview(),
	}

	# grab all contexts and bind each to numbers (only for the webview)
	for idx, context in enumerate(voice.talon.subs.values()):
		contexts[idx+1] = context
		keymap.update({str(idx+1): create_context_mapping(context)})

	webview_context.keymap(keymap)
	webview_context.load()

	webview.render(templates['contexts'], contexts = contexts, actives = voice.talon.active)
	webview.show()
	

def find_and_show(m):
	# TODO: figure out how to directly grab the name to use in show_commands…
	find = m.dgndictation[0]._words[0]
	if find in voice.talon.subs.keys():
		show_commands(voice.talon.subs[find])

def format_action(action):
	if isinstance(action, list):
		return [ a.data if isinstance(a, talon.voice.Key) else a for a in action ]
	elif isinstance(action, talon.voice.Key):
		return action.data
	elif isinstance(action, str):
		return action
	else:
		return ""

def show_commands(context):
	# what you say is stored as a trigger
	mapping = {}
	for trigger in context.triggers.keys():
		action = context.mapping[context.triggers[trigger]]
		mapping[trigger] = format_action(action)

	keymap = {
		'(0 | quit | exit | escape)': lambda x: close_webview(),
		'up': Key('pgup'),
		'down': Key('pgdown'),
	}

	webview_context.keymap(keymap)
	webview_context.load()

	webview.render(templates['commands'], context_name=context.name, mapping=mapping)
	webview.show()


keymap = {
	'show alphabet': show_alphabet,
	'show commands <dgndictation>': find_and_show,
	'show context': show_contexts,
}

ctx.keymap(keymap)