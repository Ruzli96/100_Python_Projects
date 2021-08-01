# Calculates and displays the total amount + tip paid per person

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total of your bill? \n$"))
split_number = float(input("How many people would you like this bill to be split among?\n"))
tip = float(input("What is your tip percentage? 10, 12, or 15?\n"))
amount_per = total_bill/split_number
tip_amount_per = (amount_per*(tip/100)) + amount_per
print(f'Each person should pay\n${round(tip_amount_per, 2)}')