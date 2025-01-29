"""
Calculate sum of even numbers from 1 to 100, including 1 and 100:
"""

sum = 0
for i in range(1, 101):
    if i%2 == 0:
        sum += i
print(sum)

"""
Alternatively,
"""
print()


sum2 = 0
for i in range(1, 101, 2):
    sum2 += i
print("sum using step_size 2 :", sum2)
