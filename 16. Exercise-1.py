weight = int(input("Enter weight in kgs : "))
height_cms = int(input("Enter height in cms : "))
height = height_cms/100

BMI = weight/(height * height)

print(BMI)
print("Your BMI is : ", int(BMI))

"""
SAMPLE OUTPUT -
Enter weight in kgs : 50
Enter height in cms : 168
17.71541950113379
Your BMI is :  17
"""
