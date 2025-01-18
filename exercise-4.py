"""
WAP to indicate users whether they are healthy or not based on their BMI value.
"""

weight = float(input("Enter your weight in kgs : "))
height = int(input("Enter your height in cms : "))

BMI = float(weight/((height/100)**2))
BMI = round(BMI, 1)
print()

if BMI < 18.5:
    print(f"Your BMI is {BMI}, so you are underweight.")
elif BMI >= 18.5 and BMI < 24.9:
    print(f"Your BMI is {BMI}, so you are healthy.")
elif BMI >= 25 and BMI < 29.9:
    print(f"Your BMI is {BMI}, so you are overweight!")
elif BMI >= 30 and BMI < 40:
    print(f"Your BMI is {BMI}, so you fall into Obese category!!")
else:
    print(f"Your BMI is {BMI}, so you fall into severe obesity category!!!")

print()
print("Being healthy is primary, everything rest comes after and over it.")
print()