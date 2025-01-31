# 1.
print(len("Mihika's Book"))

"""
OUTPUT -
13
"""

# 2.
print(len("90299"))
# following will give a TypeError:
#print(len(90299))

"""
OUTPUT -
5
"""

# 3.
length = len("Mahira Pandey")
# will give TypeError: can only concatenate str (not "int") to str
# print("This name has" + length + "characters")
print("This name has " + str(length) + " characters!")

"""
OUTPUT -
This name has 13 characters!
"""

# 4.
length = len("Mahira Pandey")
print(f"Data type before type casting : {type(length)}")

new_length = str(length)
print(f"Data type of length after type casting : {type(new_length)}")

"""
OUTPUT -
Data type before type casting : <class 'int'>
Data type of length after type casting : <class 'str'>
"""

# 5.
print(10+10)
print("10" + "10")
print(int("10") + int("10"))

"""
OUTPUT -
20
1010
20
"""

# 6.
name = "Mahira"
print(10 + name) 

"""
OUTPUT -
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

# 7.
name = "Mahira"
print(10 + int(name))

"""
OUTPUT -
ValueError: invalid literal for int() with base 10: 'Mahira'
"""

# 8.
name = "123"
print(10 + int(name))

"""
OUTPUT -
133
"""

# 9.
no1 = input("Enter 1st digit of no.: ") # this will take digit as string and not as a number
no2 = input("Enter 2nd digit of no.: ")
sum = no1 + no2 # since no1 and no2 digits were strings, sum will perform string concatenation i.e. 2 + 3 = 23 as 2 and 3 are of str data type
print("sum = ", sum)

"""
OUTPUT-
Enter 1st digit of no.: 5
Enter 2nd digit of no.: 7
sum = 57
"""

# 10.
no1 = input("Enter 1st digit of no.: ") # this will take digit as string and not as a number
no2 = input("Enter 2nd digit of no.: ")
sum2 = int(no1) + int(no2)
print("type-casting input sum, sum 2 = ", sum2)

"""
OUTPUT -
Enter 1st digit of no.: 8
Enter 2nd digit of no.: 7
type-casting input sum, sum 2 = 15
"""

# 11.
'''
following is not the correct format:
no4 = input(int("Enter a number: ")) ❌
'''
no3 = int(input("Enter a number: "))
no4 = int(input("Enter a no.: "))
sum = no3 + no4
print("sum = ", sum)

"""
OUTPUT -
Enter a number: 21
Enter a no.: 34
sum = 55
"""
