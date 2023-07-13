# This is a sample Python script.
print("Welcom to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total = (bill + (bill * (percentage / 100))) / people
format_total = "${:,.2f}".format(total)
print(f"Each person should pay: {format_total}")