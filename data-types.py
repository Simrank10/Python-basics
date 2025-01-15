print("That's how hex and oct num are printed...")
print(0x123)
print(0o123)

print()
print("INTEGER NUMBERS")
var_1 = 127482942830429734829891801
var_2 = 100
print(var_1)
print(var_1 + 193933)
print(var_1 + 9980.8999)

print(var_2 + 10.99)
print(var_2 + 10.90)

print(var_1 + var_2)

print()
print("checking the datatype of int using type() function...")
print(type(var_1))
print(type(var_1 + var_2))
print(type(var_2 + 100))

print()
print("FLOAT NUMBERS")
print(type(var_2 + 300.99999))

print()
print("STRING DATA TYPE")
name = "Mihika Pandey"
profession = "Student"
name_1 = "Mihika's"

uid = 10
uid_1 = "10"

print(name)
print("calling charc from string: ", name[0], name[5])
print("Intial of her surname: ", name[7])
print()
print(type(name))
print(type(name + " " + profession))

print(name + profession)
#print(name + profession + uid) --- error
print(name + profession + uid_1)
print(name + " " + profession + " " + uid_1)

print("Mihika's book is much \"pretty\"!")
print()
print("Mihik's \nbook")
print()
print(5 * "Mihika is very creative!")
print()
print(5 * "Mihika is very creative! ") # adding space between next repetation print
print()
print("Mihika is very creative\n" * 5) # printing repetation in next line!

print("1234" + "56789")
#print("123" + "456" + 789) will give error


print()
print("BOOLEAN DATA TYPE")
var_b = True
print(var_b)
print(type(var_b))

"""
this will give a NameError bec of "true"
var_b = true
print(var_b)
print(type(var_b))
"""
print()
a = 100
b = 56
var_bool = a<b
print(var_bool)
print(type(var_bool))
