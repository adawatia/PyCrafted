# python3
# bulletPointAdder.py - - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip #* Module to interact with system copy and paste
text = pyperclip.paste() #* Get what  is copied in clipboard last time
lines = text.split('\n') #* Slpit copied lines 
for i in range(len(lines)): #* To add * in everyline
    lines[i] = '*' + lines[i]
    
text = '\n'.join(lines) #* Join all lines into one
pyperclip.copy(text) #* send modilied text to clipboard


