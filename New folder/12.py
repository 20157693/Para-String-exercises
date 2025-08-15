# Display all indices an asked letter occurs in an asked sentence.

prompt = input("State the sentence:\n")
letter = input("State the letter:\n")

compensation = 0
while letter in prompt:
    index = prompt.find(letter)
    print(prompt.find(letter) + compensation)
    prompt = prompt[:index].replace(letter, '')\
    + prompt[index+1:]
    compensation += 1

    # print(prompt) # For debugging
    # input("    ") # For debugging