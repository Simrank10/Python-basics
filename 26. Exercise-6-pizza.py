"""
WAP for pizza ordering where price for
small pizza - 100 Rs
medium pizza - 200 Rs
large pizza - 300 Rs

Paneer toppings for small pizza - 30 Rs
Paneer toppings for medium or large pizza - 50 Rs

Extra cheese top toppings for any size - 20 Rs
"""

print()
print("Welcome to Patsey's Pizza store!")
print()

size = input("Choose the pizza size you want to order (Small, Medium or Large) : ")
bill_amount = 0
print()

if size == "small" or size == "Small" or size == "S" or size == "s" or size == "SMALL":
    bill_amount = 100
    print(f"Small-sized pizza cost {bill_amount} Rs without toppings!")
elif size == "medium" or size == "Medium" or size == "MEDIUM" or size == "M" or size == "m":
    bill_amount = 200
    print(f"Medium-sized pizza cost {bill_amount} Rs without toppings!")
else:
    bill_amount = 300
    print(f"Large-sized pizza cost {bill_amount} Rs without toppings!")

print()
paneer_toppings = input("Do you want paneer toppings to your pizza? (Yes/No)")
print()
if paneer_toppings == "Yes" or paneer_toppings == "yes" or paneer_toppings == "Y" or paneer_toppings == "y":
    if size == "small" or size == "Small" or size == "S" or size == "s" or size == "SMALL":
        bill_amount += 30
        print("Paneer toppings on small-sized pizza charges 30 Rs.")
        print(f"Small-sized pizza cost {bill_amount} Rs on paneer toppings!!")
    elif size == "medium" or size == "Medium" or size == "MEDIUM" or size == "M" or size == "m":
        bill_amount += 50
        print("Paneer toppings on medium-sized pizza charges 50 Rs.")
        print(f"Medium-sized pizza cost {bill_amount} Rs on paneer toppings!!")
    else:
        bill_amount += 50
        print("Paneer toppings on large-sized pizza charges 50 Rs.")
        print(f"Large-sized pizza cost {bill_amount} Rs on paneer toppings!!")

print()
extra_chess = input("Do you wish having extra-cheese to your pizza?")
bill_amount += 20
print("Extra-cheese add-on to your pizza charges 20 Rs")

print()
print("---------TOTAL BILL--------")
print(f"Total amount to be paid for your pizza is {bill_amount} Rs")
print("Thanks for ordering Pizza from us, we bake with love exclusively for you!")
print()

"""
SAMPLE OUTPUT -
