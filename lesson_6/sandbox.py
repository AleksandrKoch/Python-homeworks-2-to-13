# Challenge 5
# Reverse a string
#
# You're part of a team working on analyzing customer reviews for a new video game.
# Due to a software glitch, some reviews have been recorded in reverse with punctuation
# at the beginning instead of the end. Your task is to correct these reviews so that they
# are in the correct order and the punctuation is appropriately placed at the end of the
# sentence or word.
#
# Example: "tcefreP!" -> Perfect!

review_iverted = "tcefreP!"
review_fixed = review_iverted[len(review_iverted)-2::-1] + review_iverted[len(review_iverted)-1:]
print(review_fixed)





