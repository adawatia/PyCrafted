user_input = input("Enter a Phrase: ")
text = user_input.split()
acronym = "".join(word[0].upper() for word in text)
print(acronym)