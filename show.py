import plistlib
import string
import subprocess
import talon
import re
from pprint import pprint
from collections import OrderedDict
from talon import voice
from talon.voice import Context, Key
from talon.webview import Webview
from user import basic

ctx = Context('show')

webview_context = Context('web_view')

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
	html {
		height: 100%;
	}
	body {
	    padding: 0;
	    margin: 0;
	    font-size: 14px;
	    max-height: 100%;
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
	alphabet = list(zip(basic.alpha_alt, string.ascii_lowercase))

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
	
mapping = {
	'pearl': 'perl',
	'i term': 'iterm',
	'lack': 'slack',
	'chrome': 'googlechrome',
}

def clean_word(word):
	# removes some extra stuff added by dragon, e.g. 'I\\pronoun'
	return str(word).split('\\', 1)[0]

def find_and_show(m):
	# TODO: figure out how to directly grab the name to use in show_commands…
	words = [ clean_word(w) for w in m.dgndictation[0]._words]

	find = "".join(words).lower().replace(" ", "")
	find = mapping.get(find, find)

	contexts = { k.lower(): v for k, v in voice.talon.subs.items() }

	if find in contexts:
		show_commands(contexts[find])
		return

	# maybe context name is snake case
	find = "_".join(words).lower()
	if find in contexts:
		show_commands(contexts[find])

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

	# ignore issues if something's wrong getting monitor dimensions
	# try:
	webview.resize(x=20, y=20, w=int(display_width)-40, h=int(display_height)-40)
	# except:
	# 	pass
	webview.render(templates['commands'], context_name=context.name, mapping=mapping)
	webview.show()


keymap = {
	'show alphabet': show_alphabet,
	'show [commands] <dgndictation>': find_and_show,
	'show context': show_contexts,
}

ctx.keymap(keymap)

def get_monitor():
	displays = subprocess.check_output(["system_profiler", "-xml", "SPDisplaysDataType"])
	property_list_items = plistlib.loads(displays)[0]["_items"]
	for item in property_list_items:
		for driver in item["spdisplays_ndrvs"]:
			if "spdisplays_main" in driver:
				resolution = driver["_spdisplays_resolution"]
				matched = re.match("(\d.*) x (\d.*)", resolution)
				return matched.groups()

display_width, display_height = get_monitor()