# Output all characters from asked prompt as capitals.

prompt = input("State the sentence:\n")

new_sentence = ''
for x in prompt:
    new_sentence += x.capitalize()

print(new_sentence)
