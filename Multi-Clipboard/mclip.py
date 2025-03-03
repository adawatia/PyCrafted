#! python3
# mclip.py - A multi-clipboard program.
TEXT =  {
    'agree':"""Yes, I agree. That sound fine to me.""",
    'busy':"""Sorry, can we do this later this week or next week?""",
    'upsell':"""Would you consider making this monthly donation?"""
}

import sys, pyperclip
if len(sys.argv) < 2:
    print(f"Usage: python mclip.py [keyphrase] - copy phase text")
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard.")
else:
    print(f"There is no text for {keyphrase}")
