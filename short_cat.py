from talon.voice import Key, Context

ctx = Context('short_cat')

# Quickstart

# 1. `Cmd+Shift+Space` to activate
# 2. Enter a few letters of what you want to click. Examples:
#     - `lt` for `Language & Text`
#     - `lang` will also work
#     - `sa` for `Show All`
#     - Shortcat will only search from the beginning of words for queries under four letters.
#         - `bar` will not match `Foobar`, but will match `FooBar`, `Foo Bar` or `Batman and Robin`.
#     - When the query is over four letters, then it will start doing exact matches. `commend` will match `Recommend`
# 3. To **select an element**, hold `Control` and type in the shortcut highlighted on the field.
# 4. **Action** the element:
#     - `Enter` to **click**.
#     - To **double-click**, tap `Enter` twice in quick succession.
#     - **Modifiers** also work, so if you wanted to `Command+Click`, simply hit `Command+Enter`.
#     - To **hover** over an element, tap `Control`. Double tap `Control` to **focus** the element.

ctx.keymap({
	'short cat': Key("cmd-shift-space"),
})
