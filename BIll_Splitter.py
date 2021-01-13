print("Welcome to the tip calculator")
# asking for total bill
bill=float(input("What is the total bill :\n"))
# asking for tip %
percent=int(input("What percentage tip would you like to give? 10,12 or 15\n"))
#asking for number of people
no_people=int(input("How many people to split bill ?\n"))
# calculations
total_bill=(bill+(bill*percent/100))/no_people
total_bill=round(total_bill , 2)
print(f"Each person should pay: {total_bill}")