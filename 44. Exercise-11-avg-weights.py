"""
Python program to calculate average weight from a list of heights ( Don't use sum() and len() functions and take use input using input() function)**
hint: use split() and range() functions
"""

weight = input("Enter weights : ")
weight_list = weight.split(", ")
print(weight_list)

count = 0
for num in weight_list:
    count += 1
print(count)

for i  in range(0, count):
    weight_list[i] = int(weight_list[i])

sum = 0
for weights in weight_list:
    sum += weights
print(sum)
print(sum/count)
print(round(sum/count))
