miles = int(input("Enter the number of miles: "))
hours = int(input("Enter the total number of hours: "))

# Calculating average speed
average_speed = miles / hours

# Formatting and displaying the result
# (Your code here)
average_speed = str(average_speed)
decimal_position = average_speed.find(".")
print(decimal_position)
rounded_speed = average_speed
if "." in average_speed:
    rounded_speed = average_speed[:decimal_position]+"."+average_speed[decimal_position+1]
else:
    rounded_speed = average_speed

print(f"The average speed is {rounded_speed} miles per hour")