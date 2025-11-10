# Create a program that will calculate your monthly expenses.
# Each expense amount is represented by a variable.

rent = 1200
utilities = 300
groceries = 450
entertainment = 200

def monthly_expences(expense1, expense2, expense3, expense4):
    return expense1 + expense2 + expense3 + expense4

print(f"Total expences {monthly_expences(rent, utilities, groceries, entertainment)}")

# Calculate the total monthly expenses and determine the
# percentage of rent relative to the total expenses.
def rent_percentage(rent, utilities, groceries, entertainment):
    percentage = 100 * (rent / (utilities + groceries + entertainment))
    return percentage

print(f"Rent percentage is {rent_percentage(rent, utilities, groceries, entertainment)}")
# Hint: to count the percentage of rent, count total monthly
# expenses first, then divide expenses for rent by the total
# expenses and multiply by 100.
