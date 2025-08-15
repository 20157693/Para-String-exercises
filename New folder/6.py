# Find 'code' in asked sentence.

prompt = input("State the sentence:\n")

found = prompt.find('code')
if found != -1:
    print(found)
else:
    print("I guess you had other things to talk about")

