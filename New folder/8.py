# Check if word is in asked sentence.

prompt = input("State the sentence:\n")
word = input("State the word:\n")

if word in prompt:
    print('The word is inside.')
else:
    print('The word is not inside.')