# 1.
print("Arithmetic sum: ", 8 + 2)
"""
OUTPUT-
Arithmetic sum:  10
"""

print("Arithmetic subtraction: ", 8 - 2)
print()
print("Arithmetic multiplication: ", 8*2)
print()
print("Arithmetic exponential: ", 8**2)
print()
print("Arithmetic division: ", 8/2)
print()
print("Arithmetic modulus: ", 8%2)
print()
print("Arithmetic floor division: ", 8//2)
print()
print("using PEMDAS (PARENTHESIS OF EXPONENTIAL, MULTIPLICATION, DIVISION, ADDITION AND SUBTRACTION)")
print("Solution of 5 + 2 * 3 - 1 + 10/5 : ", 5 + 2 * 3 - 1 + 10/5)
print()
print("Solution of 5 + 2 * (3 - 1) + 10/5 : ", 5 + 2 * (3 - 1) + 10/5)
print()


print("BMI calculator")
height_mtrs = float(input("Enter your height in cms: "))
height = height_mtrs/100
weight = int(input("Enter your weight in kgs: "))
BMI = weight/(height)**2
print("your BMI is: ", BMI)
