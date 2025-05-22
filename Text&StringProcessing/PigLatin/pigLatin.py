#! python3
message = input("Enter the English message to translate to Pig Latin: ")
VOWELS = ('a','e','i','o','u')
pigLatin = [] # Words of pig-latin language.
for word in message.split():
    prefixNonLetters = ""
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    
    suffixNonLetters = ""
    
    while not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1] 
        
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    
    word = word.lower()
    
    prefixConsonants = ""
    
    while len(word) > 0 and word[0] not in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
        
    if prefixConsonants != "":
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    
    if wasUpper:
        word += word.upper()
        
    if wasTitle:
        word += word.title()
        
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
    
print(f"PigLatin 🐷:{" ".join(pigLatin)}")