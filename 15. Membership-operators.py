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
space in name :  True
"""

# 4.
name = "Mahira Tripathi"
print("a in name : ", "a" in name)
"""
OUTPUT -
a in name :  True
"""

# 5.
name = "Mahira Tripathi"
print("pat in name : ", "pat" in name)
"""
OUTPUT -
pat in name :  True
"""

# 6.
name = "Mahira Tripathi"
print("tripathi not in name : ", "tripathi" not in name)
"""
OUTPUT -
tripathi not in name :  True
"""

# 7.
name = "Mahira Tripathi"
print("hira in name : ", "hira" in name)
"""
OUTPUT -
hira in name :  True
"""

# 8.
name = "Mahira Tripathi"
print(id(name[1]))
"""
OUTPUT -
2687214864688
"""

# 9.
name = "Mahira Tripathi"
print(id(name[5]))
"""
OUTPUT -
2687214864688
"""

# 10.
name = "Mahira Tripathi"
print(id(name[11]))
"""
OUTPUT -
2687214864688
"""

# 11.
name = "Mahira Tripathi"
print(id(name[10]))
# if you could see memory location for "a" is same for all a's present in name
"""
OUTPUT -
2687212813360
"""

# 12.
name = "Mahira Tripathi"
print(id("p"))
"""
OUTPUT -
2687212813360
"""

# 13.
roll_no = [12, 24, 56, 79, 10, 2, 1]
print("13 in roll_no : ", 13 in roll_no)
print("2 in roll_no : ", 2 in roll_no)
print("14 not in roll_no : ", "14" not in roll_no)
"""
OUTPUT -
13 in roll_no :  False
2 in roll_no :  True
14 not in roll_no :  True
"""
