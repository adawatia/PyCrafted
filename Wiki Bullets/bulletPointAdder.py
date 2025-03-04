# python3
# bulletPointAdder.py - - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()
# TODO: Seperate lines and add stars
pyperclip.copy(text)