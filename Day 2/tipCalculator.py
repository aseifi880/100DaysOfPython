print("Welcome to the tip calculator.")
billAmount = float(input("what was the total bill? "))
tipPercent = float(input("what percent tip would you like to give? "))
numPeople = float(input("how many people to split the bill with? "))
sharePerPerson = ( billAmount * ( 1 + tipPercent / 100 ) ) / numPeople
print(f"Each person should pay : {round(sharePerPerson, 2)}")