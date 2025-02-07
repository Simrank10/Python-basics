"""
Check whether a given year is leap year or not?
"""

year = int(input("Enter a year you want to check for : "))
print(f"Okay, Let's check for {year} year...")

if year % 4 == 0:
    if year % 100 ==0:
        if year % 400==0:
            print(f"The year {year} is a leap year!")
        else:
            print(f"The year {year} is not a leap year.")
    else:
        print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year!")

print("Leap year is year which is completely divisible by 4. Also, if year is not divisible "
      " by 100, its a leap year and if divisible by 100 we check whether it is divisible by 400" 
      " too conclude its a leap year")


"""
OUTPUT - 
Enter a year you want to check for : 2034
Okay, Let's check for 2034 year...
The year 2034 is not a leap year!
Leap year is year which is completely divisible by 4. Also, if year is not divisible  by 100, its a leap year and if divisible by 100 we check whether it is divisible by 400 too conclude its a leap year
"""
