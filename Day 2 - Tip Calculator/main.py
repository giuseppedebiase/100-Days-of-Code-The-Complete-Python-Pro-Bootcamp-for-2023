bill = float(input("What was the total bill? "))
tipperc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
#Calculates the total amount of bill pluss tip
tot = (bill+bill*tipperc/100)
numpeople = int(input("How many people to split the bill? "))
totround = round(tot/numpeople, 2)
totround = "{:.2f}".format(totround)
print(f"Each person should pay: ${totround}")
