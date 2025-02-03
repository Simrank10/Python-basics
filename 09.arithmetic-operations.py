# 1.
print("Arithmetic sum: ", 8 + 2)
"""
OUTPUT -
Arithmetic sum:  10
"""

# 2.
print("Arithmetic subtraction: ", 8 - 2)
"""
OUTPUT -
Arithmetic subtraction:  6
"""

# 3.
print("Arithmetic multiplication: ", 8*2)
"""
OUTPUT -
Arithmetic multiplication:  16
"""

# 4.
print("Arithmetic exponential: ", 8**2)
"""
OUTPUT -
Arithmetic exponential:  64
"""

# 5.
print("Arithmetic division: ", 8/2)
"""
OUTPUT -
Arithmetic division:  4.0
"""

#6. 
print("Arithmetic modulus: ", 8%2)
"""
OUTPUT -
Arithmetic modulus:  0
"""

# 7.
print("Arithmetic floor division: ", 8//2)
"""
OUTPUT -
Arithmetic floor division:  4
"""

# 8.
print("using PEMDAS (PARENTHESIS OF EXPONENTIAL, MULTIPLICATION, DIVISION, ADDITION AND SUBTRACTION)")
print("Solution of 5 + 2 * 3 - 1 + 10/5 : ", 5 + 2 * 3 - 1 + 10/5)
"""
OUTPUT -
using PEMDAS (PARENTHESIS OF EXPONENTIAL, MULTIPLICATION, DIVISION, ADDITION AND SUBTRACTION)
Solution of 5 + 2 * 3 - 1 + 10/5 :  12.0
"""

# 9.
print("Solution of 5 + 2 * (3 - 1) + 10/5 : ", 5 + 2 * (3 - 1) + 10/5)
"""
OUTPUT -
Solution of 5 + 2 * (3 - 1) + 10/5 :  11.0
"""


print("BMI calculator")
height_mtrs = float(input("Enter your height in cms: "))
height = height_mtrs/100
weight = int(input("Enter your weight in kgs: "))
BMI = weight/(height)**2
print("your BMI is: ", BMI)
