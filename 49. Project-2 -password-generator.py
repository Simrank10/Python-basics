import random

chars = ['a', "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
        "A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L", "M", 
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

spec_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ".", "?", "<", ">", "-"]

nums = ["1", "2", "3", "4", '5', '6', '7', '8', '9', '0']

print("Let's generate a password for you!")

char_en = int(input("How many characters you need in your password? "))
spec_char_en = int(input("How many special characters you need in your password? "))
num_en = int(input("How many numbers you need in your password? "))

password = ""

for i in range(1, char_en+1):
    char = random.choice(chars)
    password += char

for i in range(1, spec_char_en+1):
    spec_char = random.choice(spec_chars)
    password += spec_char

for i in range(1, num_en+1):
    num = random.choice(nums)
    password += num

print(password)

"""
Strong shuffled char, special char and numbers in the password!
"""

password_list = []

for i in range(1, char_en+1):
    char = random.choice(chars)
    password_list += char

for i in range(1, spec_char_en+1):
    spec_char = random.choice(spec_chars)
    password_list += spec_char

for i in range(1, num_en+1):
    num = random.choice(nums)
    password_list += num

#print(password_list)

random.shuffle(password_list)
#print(password_list)

shuffled_password = ""
for i in password_list:
    shuffled_password += i

print(shuffled_password)

