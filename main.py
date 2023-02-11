print("Welcome to the tip calculator")
amount=input("What was total bill?")
percentage=input("What percentage tip would you like to give? 10,12, or 15?")
people=input("How many people to splite the bill?")
percentage=int(percentage)/100+1
person_amount=float(amount)*percentage/int(people)
print(f"Each person should pay: {round(person_amount,2)}")