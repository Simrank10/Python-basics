# 1.
print("Arithmetic sum: ", 8 + 2)
"""
OUTPUT-
Arithmetic sum:  10
"""

# 2.
print("Arithmetic subtraction: ", 8 - 2)


# 3.
print("Arithmetic multiplication: ", 8*2)


# 4.
print("Arithmetic exponential: ", 8**2)

# 5.
print("Arithmetic division: ", 8/2)


#6. 
print("Arithmetic modulus: ", 8%2)


# 7.
print("Arithmetic floor division: ", 8//2)

# 8.
print("using PEMDAS (PARENTHESIS OF EXPONENTIAL, MULTIPLICATION, DIVISION, ADDITION AND SUBTRACTION)")
print("Solution of 5 + 2 * 3 - 1 + 10/5 : ", 5 + 2 * 3 - 1 + 10/5)


# 9.
print("Solution of 5 + 2 * (3 - 1) + 10/5 : ", 5 + 2 * (3 - 1) + 10/5)


print("BMI calculator")
height_mtrs = float(input("Enter your height in cms: "))
height = height_mtrs/100
weight = int(input("Enter your weight in kgs: "))
BMI = weight/(height)**2
print("your BMI is: ", BMI)
