name = "Mahira Tripathi"
print("m in name : ", "m" in name)
print("M in name : ", "M" in name)
print("space in name : ", " " in name)
print("a in name : ", "a" in name)
print("pat in name : ", "pat" in name)
print("tripathi not in name : ", "tripathi" not in name)
print("hira in name : ", "hira" in name)
print(id(name[1]))
print(id(name[5]))
print(id(name[11]))
print(id(name[10]))
# if you could see memory location for "a" is same for all a's present in name 
print(id("p"))

roll_no = [12, 24, 56, 79, 10, 2, 1]
print("13 in roll_no : ", 13 in roll_no)
print("2 in roll_no : ", 2 in roll_no)
print("14 not in roll_no : ", "14" not in roll_no)