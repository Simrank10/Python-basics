"""
For a series of numbers from 1 to 100, the task is to print,

“FizzBuzz” if i is divisible by 3 and 5,
“Fizz” if i is divisible by 3,
“Buzz” if i is divisible by 5
“i” as a string, if none of the conditions are true.
"""

for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("fizz")
    else:
        print(i)


print()
print("THE SAME TASK BUT THIS TIME WE WILL TAKE USER INPUT!")

i = int(input("Enter where to start range : " ))
j = int(input("Enter where to stop range : " ))
k = int(input("Enter step-size for range : " ))

for i in range(i, j, k):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("fizz")
    else:
        print(i)