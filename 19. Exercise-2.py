"""
WAP to find out how many days, weeks, months, we have left if we live untill 90 years old?
o/p expected :- you have a years, b months, c days left!
"""

age = int(input("Enter your age : ")) 
"""
Enter your age : 20
"""

years_left = 90 - age
months_left = years_left*12
days_left = years_left*365
weeks_left = years_left*52

print(f"If you live until 90 years old, you have {months_left} months left, {weeks_left} weeks left, {days_left} days left!!!!")
"""
OUTPUT -
If you live until 90 years old, you have 840 months left, 3640 weeks left, 25550 days left!!!!
"""
