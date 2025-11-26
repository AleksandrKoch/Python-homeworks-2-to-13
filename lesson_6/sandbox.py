# Exercise 2. The Card Deck ♦️♥️♠️♣️

# You will be provided with a couple lists that contain the cards for a card deck.
# One of the lists contains the numbers, and the other one contains the faces.

# You will be asked to fill in the blanks to print out certain cards for a card game you've been working on.

# 🔥 Tip: You might want to stitch them together first.

# Here are the card decks.
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
faces = ['J', 'Q', 'K']

# Concatenate them first.
card_deck = numbers + faces

# Print out the numbers 1 to 6.
print(card_deck[:6])

# Print out the last 3. Do it using POSITIVE indexes.
print(card_deck[10:])

# Print out the last 3 (same as before), but using NEGATIVE indexes.
print(card_deck[-3:])

# Print out everything EXCEPT the first and last.
print(card_deck[1:-1])

# What would you use so the printout includes the following:
# Hint: It's every third card of the full deck.
# ['1', '4', '7', '10', 'K']
print(card_deck[::3])

# Print out the EVEN numbers. No faces.
print(card_deck[1:10:2])
