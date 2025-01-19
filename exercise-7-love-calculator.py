print()
print("Let's check the love score!")
print()
name_1 = input("Enter name : ")
print()
name_2 = input("Enter his/her name : ")

name_1 = name_1.lower()
name_2 = name_2.lower()

t = name_1.count("t") + name_2.count("t")
#print(t)
r = name_1.count('r') + name_2.count("r")
#print(r)
u = name_1.count("u") + name_2.count("u")
#print(u)
e = name_1.count("e") + name_2.count("e")
#print(e)

l = name_1.count("l") + name_2.count("l")
#print(l)
o = name_1.count("o") + name_2.count("o")
#print(o)
v = name_1.count("v") + name_2.count("v")
#print(v)
e = name_1.count("e") + name_2.count("e")
#print(e)

true = t+r+u+e
love = l+o+v+e

true_love = str(true) + str(love)
true_love = int(true_love)

print()

if true_love < 10 or true_love > 90:
    print(f"Your love score is {true_love}%, you guys go together like coke and mentos!")
elif true_love >= 40 and true_love <= 60:
    print(f"Your love score is {true_love}%, you guys are just alright!")
else:
    print(f"Your love score is {true_love}%")

print()
print("Infact, these results may vary in reality."
      "\nWe aren't astrologers and we don't intend to underestimate or overestimate anyone's true feelings.")
print("Okay, bye!")
print()