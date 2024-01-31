print("Welcome to the tip calculator!")
bill = float(input("What was the total bill amount?"))
split = float(input("How many people split the bill?"))
perc = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
perctotal = bill * (perc/100)
totalpay = (bill + perctotal) / split

#get total pay as to 2 decmials
totalpay = "{:.2f}".format(totalpay)
print(f"Each person should pay: ${totalpay}")
