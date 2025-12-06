# Returning Values
# Define a validator function that you can use to determine if a word is longer than 8 characters.
# After creating the function, make sure to test it. Create a list of words and iterate over this
# list using a for loop.

# Tip: Validator functions return True / False which we can use in conditionals to do things like print a message.

def validator(word):
    if len(word) > 8:
        return True
    else:
        return False

list_of_words = ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678', '123456789', '']

for word in list_of_words:
    if validator(word) == False:
        print(f"For word {word} length is less or equal to 8 symbols")
    else:
        print(f"For word {word} length is greater than 8 symbols")