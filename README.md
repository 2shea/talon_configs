# Talon Modules for use with [Talon](https://talonvoice.com/)

These modules contain voice and noise commands to be used with Talon, a hands-free input replacement. Some modules are meant to be used with the Tobii 4C eye tracker, but it is not required for most commands.

Some modules were originally copied from [Talon Community](https://github.com/dwiel/talon_community).


# Prerequisites
- Install Talon
- Install Dragon (most commands may also work with the free built-in voice engine)
- Microphone (built in microphone won't produce great results, a good microphone makes a significant difference)

Follow the [Getting Started](https://talonvoice.com/docs/) section of the Talon docs.

# Installing
Clone this repository into `~/.talon/user`. Any files in this directory will automatically be loaded into Talon. 

# Getting Started
Each file will have a Context (e.g., "sublime", "slack"). A Context is a logical grouping of commands which can be active globally or only under certain conditions (e.g., when a specific app is in focus, when working in a file with a specific file extension, or even when a specific song is playing on spotify).

All noise or voice commands for a context will be inside of a dictionary passed into the `keymap` function of the context.

```
from talon.voice import Context, Key

context = Context("example", bundle="com.example")
context.keymap({

	# voice command => action
	"say this": "talon will do this",

	# generate a string
	"get status": "git status",

	# press keys using Key
	"space": Key("space"),

	# press multiple keys
	"copy": Key("cmd-c"),

	# multiple actions 
	"args": ["()", Key("left")],
})
```


