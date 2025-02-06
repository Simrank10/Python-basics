# 1. Nested if statements

num = int(input("Enter a number : "))
if num <=100:
    print("Number is less than 100.")
    if num%2==0:
        print("Number is multiple of 2")
    if num%3==0:
        print("Number is multiple of 3")
    if num%5==0:
        print("Number is multiple of 5")
    if num%7==0:
        print("Number is multiple of 7")
    if num>1 and num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:
        print("Number is prime!")
else:
    print("Number is not less than or equal to 100!")
print()

"""
OUTPUT -
Enter a number : 487
Number is not less than or equal to 100!
"""

# 2. Nested if, elif and else statements

height = int(input("Enter your height in cms : "))
if height>100:
    print("You can ride!")
    age = int(input("Enter your age : "))
    if age <12:
        print("Please, pay 100 rs!")
    elif age <=18:
        print("Please, pay 150 rs!")
    else:
        print("Please pay 250 rs!")

else:
    print("You can't ride!")

print("Bye, thanks for choosing us!")

"""
OUTPUT -
Enter your height in cms : 170
You can ride!
"""
