"""
Python program to find maximum number from a list of numbers ( Don't use max() and len() functions 
and take use input using input() function)
hint: use split() and range() functions .
"""

num = input("Enter numbers seperated with commas : ")
num_list = num.split(", ")
print(num_list)

count = 0
for number in num_list:
    count += 1
print(count)

for i in range(0, count):
    num_list[i] = int(num_list[i])

maximum = num_list[0]

for number in num_list:
    if number > maximum:
        maximum = number

print(maximum)
    