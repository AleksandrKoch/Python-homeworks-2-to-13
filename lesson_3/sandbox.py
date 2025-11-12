# Exercise 9: Workouts calculator
# Write a Python program that asks the user to input the number
# of minutes spent on three different exercises: cardio, strength
# training, and yoga using the input() function. Convert the input
# strings to integers using the int() function. Calculate the
# total time spent on workouts by summing up the minutes from all
# three activities. Based on the total workout time, provide a
# motivational message using an f-string that encourages the user
# to stay consistent and reach their fitness goals. Display the
# motivational message to the user.

cardio_minutes = int(input("Enter cardio time in minutes: "))
strength_minutes = int(input("Enter strength time in minutes: "))
yoga_minutes = int(input("Enter yoga time in minutes: "))
total_minutes = cardio_minutes + strength_minutes + yoga_minutes
print(f"You worked out for {total_minutes} minutes! Keep it up and stay consistent to reach your fitness goals!")