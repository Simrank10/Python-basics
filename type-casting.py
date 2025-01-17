print(len("Mihika's Book"))

print(len("90299"))

"""
following will give a TypeError:
print(len(90299))
"""

length = len("Mahira Pandey")
'''
will give TypeError: can only concatenate str (not "int") to str
print("This name has" + length + "characters")
'''
print("This name has " + str(length) + " characters!")
print()
print(type(length))
print()
new_length = str(length)
print(type(new_length))

print()
print(10+10)
print("10" + "10")
print(int("10") + int("10"))

print()
name = "Mahira"
# print(10 + name) TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(10 + int(name)) ValueError: invalid literal for int() with base 10: 'Mahira'
print()
name = "123"
print(10 + int(name))

print()
no1 = input("Enter 1st no.: ")
no2 = input("Enter 2nd no.: ")
sum = no1 + no2
print(sum)
print()

sum2 = int(no1) + int(no2)
print("type-casting input sum: ", sum2)

'''
following is not the correct format:
no4 = input(int("Enter a number: "))
'''

no3 = int(input("Enter a number: "))
no4 = int(input("Enter a no.: "))
sum = no3 + no4
print(no3 + no4)