fruit = input("Which fruit to get from supermarket? ")

if fruit == "Apple":
    print("Get it!")
else:
    print("Get Oranges if available!")


print()

marks = float(input("Enter your marks : "))

if marks < 30:
    print("You have not cleared the exam!")
    print("Needs improvement...")
    print("'Result' : FAIL")

else:
    print("Congratulations!, you've cleared your exam.")
    print("Good luck for future endeavours!")
    print("'Result' : PASSED")