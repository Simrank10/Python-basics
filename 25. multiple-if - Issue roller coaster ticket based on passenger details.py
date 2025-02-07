"""
PROBLEM -
WAP to issue a ticket and bill for a Revalish amusement park's roller coaster ride. 
People shorter than 100 cm or 3.2 feet cannot ride. 
For those who qualify, ticket prices depend on age: 
• ₹100 for children under 12, 
• ₹250 for those aged 12 to 18, and 
• ₹350 for anyone older than 18. 
If a rider wants pictures, an additional ₹50 is added to the bill.
"""

print("Welcome to Revalish Amusement Park!")
print()
print("Welcome to the roller coaster ride.... \nGet ready for an unforgettable adventure!"
      " \nBuckle up and brace yourself for the thrill!"
      " \nDouble the excitement, double the fun!")

print()
height = int(input("Enter your height in cms : "))
bill_amount = 0

if height > 100:
    print("You can ride!")
    print()
    age = int(input("Enter your age : "))
    if age <12:
        bill_amount = 100
        print(f"Your ticket cost : {bill_amount} Rs")
    elif age <= 18:
        bill_amount = 250
        print(f"Your ticket cost : {bill_amount} Rs")
    else:
        bill_amount = 350
        print(f"Your ticket cost : {bill_amount} Rs")
    
    print()
    want_photo = input("Do you want a photo? (Yes/No)")
    if want_photo == "Yes":
        print()
        print("Picture charges : 50 Rs")
        bill_amount += 50
    else:
        bill_amount
        
else:
    print("Sorry, You aren't allowed for this ride!")

print()
print("----Final Bill----")
print()
print(f"Your total bill amount to pay is {bill_amount} Rs")
print("Thanks for visting, enjoy your ride!")

"""
OUTPUT -
Welcome to Revalish Amusement Park!

Welcome to the roller coaster ride....
Get ready for an unforgettable adventure!
Buckle up and brace yourself for the thrill!
Double the excitement, double the fun!

Enter your height in cms : 170
You can ride!

Enter your age : 20
Your ticket cost : 350 Rs

Do you want a photo? (Yes/No)Yes

Picture charges : 50 Rs

----Final Bill----

Your total bill amount to pay is 400 Rs
Thanks for visting, enjoy your ride!
"""
