# 1.
fruit = input("Which fruit to get from supermarket? ")

if fruit == "Apple":
    print("Get it!")
else:
    print("Get Oranges if available!")
"""
OUTPUT -
Which fruit to get from supermarket? Chikoo
Get Oranges if available!
"""

# 2.
marks = float(input("Enter your marks : "))

if marks < 30:
    print("You have not cleared the exam!")
    print("Needs improvement...")
    print("'Result' : FAIL")

else:
    print("Congratulations!, you've cleared your exam.")
    print("Good luck for future endeavours!")
    print("'Result' : PASSED")
"""
OUTPUT -
Enter your marks : 67
Congratulations!, you've cleared your exam.
Good luck for future endeavours!
'Result' : PASSED
"""
