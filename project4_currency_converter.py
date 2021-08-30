with open("currency.txt") as f:
    lines = f.readlines()

currencydict = {}
for line in lines:
    a = line.split("\t")
    currencydict[a[0]] = a[1]
# print(currencydict)   
amount = int(input("Enter Amount: \n"))
print("Enter the name of Currency You Want To Convert This Amount To? \n Available Optons Are: \n")
[print(item) for item in currencydict.keys()]
currency = input("PLease Enter One Of These Values: \n")
print(f"{amount} INR Is Equal To {amount * float(currencydict[currency])} {currency}")
