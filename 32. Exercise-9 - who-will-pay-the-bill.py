"""
WAP which will select a random name name from the list of names and the 
person selected will have to pay for everybody's food.
"""


import random

names = str(input("Enter the names seperated with commas : "))
members = names.split(", ")

print(members)
#print(len(members))

choice = random.randint(0, len(members)-1)
#print(choice)
print(f"{members[choice]} will pay the bill!")

"""
ALTERNATIVELY, use choice!
"""

person_selected = random.choice(members)
print(person_selected) # siya


"""
SAMPLE OUTPUT -
Enter the names seperated with commas : Raghav, Siya, Mahira, Tasha, Devansh
['Raghav', 'Siya', 'Mahira', 'Tasha', 'Devansh']
Tasha will pay the bill!
"""
