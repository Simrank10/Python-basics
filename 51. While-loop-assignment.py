"""
Take input from the user and compute the sum of positive integers only. 
The program should exit as soon as the user enters a negative number or zero.
"""

#num = int(input("Enter a number > 0 : "))
sum = 0
while True:
    num = int(input("Enter a number > 0 (0 or -ve number to quit): "))
    sum += num
    print("Current Sum:", sum)
    if num <= 0:
        break
print()
print(f"The sum of positive entered numbers is {sum}")
