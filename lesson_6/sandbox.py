# Exercise 4. Bonus Round: The Speech Reverser and Counter 🎤

# Python has a handy little method that allows you to split a string.
# In its most basic form it splits a string into a list using the spaces as separators:

# Example:

# phrase = "My Name is Joseph"
# words = phrase.split()
# print(words) -> ['My', 'Name', 'is', 'Joseph']

# More information about split: https://www.w3schools.com/python/ref_string_split.asp

# Now, armed with `split()` write a program that does the following:

# - Takes a string input from the user.
# - Splits it into words.
# - Prints out the string with the words in reverse order.
# - Prints out the word count.

# Get input from the user
user_input = input('Give me a phrase')

# Split user input into words
words = user_input.split()

# Reverse the list and print it
reversed_words = list(reversed(words))
print(reversed_words)

# Print the length of the words list
print(len(words))