import string
import talon
from pprint import pprint
from collections import OrderedDict
from talon import voice
from talon.voice import Context
from talon.webview import Webview
from user import basic_keys

ctx = Context('show')
webview_context = Context('webview_context')

webview = Webview()
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
	<h3>commands</h3>
	<div class="contents">
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
	    	<td>{{ index }}</td><td>{{ context }}</td>
	    	<td>{% if context in actives %}✅{% else %}❌{%endif %}</td>
	    </tr>
	{% endfor %}
	</table>
	</div>
	'''
}

def show_alphabet(_):
	global webview_context

	alphabet = list(zip(basic_keys.alpha_alt, string.ascii_lowercase))

	webview.render(templates['alpha'], alphabet=alphabet)
	webview.show()

	keymap = {
		'(0 | quit | exit | escape)': lambda x: close_webview(),
	}

	webview_context.keymap(keymap)
	webview_context.load()

def close_webview():
    webview.hide()
    webview_context.unload()

def show_contexts(_):
	contexts = OrderedDict()

	keymap = {
		'(0 | quit | exit | escape)': lambda x: close_webview(),
	}

	for idx, context in enumerate(voice.talon.subs.values()):
		contexts[idx+1] = context

	for k, v in contexts.items():
		keymap.update({str(k+1): lambda x: show_commands(v)})

	pprint(keymap)

	# keymap.update({'right wipe %s' % k: [Key('delete')] * k for k in range(1,10)})
	# keymap.update({'%s' % i: lambda x: show_commands(contexts[i-1]) for i in range(1, len(contexts) + 1)})

	webview.render(templates['contexts'], contexts = contexts, actives = voice.talon.active)
	webview.show()
	
	webview_context.keymap(keymap)
	webview_context.load()


def show_commands(context):
	close_webview()
	pprint(context)
	# what you say is stored as a trigger
	# context = voice.talon.subs[context]
	mapping = {}
	for trigger_key in context.triggers.keys():
		# try:
		mapped_to = context.mapping[context.triggers[trigger_key]]
		if isinstance(mapped_to, talon.voice.Key):
			mapping[trigger_key] = mapped_to.data
		else:
			mapping[trigger_key] = mapped_to
		# except:
		# 	continue

	webview.render(templates['commands'], mapping=mapping)
	webview.show()

	keymap = {
		'(0 | quit | exit | escape)': lambda x: close_webview(),
	}

	webview_context.keymap(keymap)
	webview_context.load()


keymap = {
	'[show] alphabet': show_alphabet,
	# '[show] commands <dgndictation>': show_commands,
	'[show] context': show_contexts,
}

ctx.keymap(keymap)