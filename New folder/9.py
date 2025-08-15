# Function to accept two strings and outputs total with space in-between.

def sentence_appender():
    prompt = input("State the first sentence:\n")
    prompt2 = input("State the second sentence:\n")
    output = prompt + " " + prompt2
    print(output)

sentence_appender()

