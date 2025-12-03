# Multiple Parameters
# Define a function that takes two parameters, add them up and prints the sum.

# Prints: The sum of 1 + 2 = 3
# add(1, 2)

# Prints (default values might be useful): The sum of 1 + 0 = 1
# add(1)

def sum_of_two(num1=0, num2=0):
    print(f"The sum of {num1} + {num2} = {num1 + num2}")
    return num1 + num2

sum_of_two(1)

