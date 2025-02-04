# 1.
name = "Mahira Tripathi"
print("m in name : ", "m" in name)
"""
OUTPUT -
m in name :  False
"""

# 2.
name = "Mahira Tripathi"
print("M in name : ", "M" in name)
"""
OUTPUT -
M in name :  True
"""

# 3.
name = "Mahira Tripathi"
print("space in name : ", " " in name)
"""
OUTPUT -

"""

# 4.
name = "Mahira Tripathi"
print("a in name : ", "a" in name)
"""
OUTPUT -

"""

# 5.
name = "Mahira Tripathi"
print("pat in name : ", "pat" in name)
"""
OUTPUT -

"""

# 6.
name = "Mahira Tripathi"
print("tripathi not in name : ", "tripathi" not in name)
"""
OUTPUT -

"""

# 7.
name = "Mahira Tripathi"
print("hira in name : ", "hira" in name)
"""
OUTPUT -

"""

# 8.
name = "Mahira Tripathi"
print(id(name[1]))

name = "Mahira Tripathi"
print(id(name[5]))

name = "Mahira Tripathi"
print(id(name[11]))

name = "Mahira Tripathi"
print(id(name[10]))
# if you could see memory location for "a" is same for all a's present in name 
print(id("p"))


roll_no = [12, 24, 56, 79, 10, 2, 1]
print("13 in roll_no : ", 13 in roll_no)
print("2 in roll_no : ", 2 in roll_no)
print("14 not in roll_no : ", "14" not in roll_no)
