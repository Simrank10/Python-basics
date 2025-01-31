S1_name = "Sophia"
print(S1_name)

#"a" = 1
#print("a")
"""
Write a Python program to take two numbers as input, swap their values using a temporary variable, 
and display the numbers before and after swapping.
"""

no1 = input("Enter value for 1st number:")
no2 = input("Enter value for 2nd number: ")
print("no1 initially: ", no1)
print("no2 initially: ", no2)

temp = no1
no1 = no2
no2 = temp
print()
print("no1 after swap: ", no1)
print("no2 after swap: ", no2)

"""
OUTPUT -
Enter value for 1st number:2
Enter value for 2nd number: 3
no1 initially:  2
no2 initially:  3

no1 after swap:  3
no2 after swap:  2
"""
