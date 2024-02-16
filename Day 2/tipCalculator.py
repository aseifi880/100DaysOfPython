# Display a welcome message to the user
print("Welcome to the tip calculator.")

# Take user input for the total bill amount, tip percentage, and number of people
bill_amount = float(input("What was the total bill? "))
tip_percent = float(input("What percent tip would you like to give? "))
num_people = float(input("How many people to split the bill with? "))

# Calculate the amount each person should pay
total_bill_with_tip = bill_amount * (1 + tip_percent / 100)
share_per_person = total_bill_with_tip / num_people

# Display the amount each person should pay, rounded to two decimal places
print(f"Each person should pay: {round(share_per_person, 2)}")
