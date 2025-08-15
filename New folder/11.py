# Change all vowels to '*'

prompt = input("State the sentence:\n")

new_sentence = ''
vowels = ['a','e', 'i', 'o', 'u']
for x in prompt:
    if x in vowels:
        x = '*'
        new_sentence += x
    else:
        new_sentence += x

print(new_sentence)
    