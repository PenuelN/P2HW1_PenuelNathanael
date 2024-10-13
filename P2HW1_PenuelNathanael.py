# Nathanael Penuel
# 10/13/2024
# P2HW1 - Travel Expenses
# This program calculates and displays travel expenses.

# 1. Enter the total budget.
# 2. Enter the travel destination.
# 3. Enter the estimated cost of gas.
# 4. Enter the estimated cost of accommodation.
# 5. Enter the estimated cost of food.
# 6. Calculate the total expenses by adding gas, accommodation, and food costs.
# 7. Calculate the remaining balance by subtracting the total expenses from the budget.
# 8. Display the total expenses and show remaining balance.

# Asking for input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_expense = float(input("How much do you think you will spend on gas? "))
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_expense = float(input("Last, how much do you need for food? "))

# Calculating 
remaining_balance = budget - (gas + accommodation + food)

# Displaying
print("\n------------Travel Expenses------------")
print(f"{'Location:':<20} {destination:<20}")
print(f"{'Initial Budget:':<20} ${budget:<.2f}")
print(f"{'Fuel:':<20} ${gas:<.2f}")
print(f"{'Accommodation:':<20} ${accommodation:<.2f}")
print(f"{'Food:':<20} ${food:<.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance:':<20} ${remaining_balance:<.2f}")
