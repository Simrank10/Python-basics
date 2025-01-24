list1 = [1, "cust_id", [334, 332, 456, 339], 2, "names", ["Crist", "David", "Leona", "Andie"], 3, "title", ["Anderson", "Watson", "Anderson", "Watson"], 4, "gender", ["male", "male", "female", "female"]]

len_list1 = len(list1)
print(len_list1)
print()

print("accessing elements from nested list : ")
print(list1[2])
print(list1[len(list1) - 10])
print(list1[2][0])
print(list1[2][1])
print(list1[2][2])
print()

print(f"{list1[5][0]} is our customer with cust id {list1[2][0]}")
print(f"{list1[5][1]} is our customer with cust id {list1[2][1]}")
print(f"{list1[5][2]} is our customer with cust id {list1[2][2]}")
print(f"{list1[5][3]} is our customer with cust id {list1[2][3]}")
print()

print("Using slicing for nested list in a list")
print(list1[5][0:2])
print(list1[5][0:4:2])
print(list1[5][0::3])
print()

print(f"Our updated list of customers after customer churn is : {list1[5][::2]}")
print(f"According to details, {list1[5][::2]} are a couple and {list1[5][1::2]} are a couple!")
print(f"According to details, {list1[5][0]} and {list1[5][2]} are a couple and {list1[5][1]} and {list1[5][3]} are a couple!")
print()

print(f"Details with us, for customer with cust ID {list1[2][0]} is Name :", list1[5][0] + " " + list1[8][0] + ",", f"Gender : {list1[11][0]}")
print(f"Details with us, for customer with cust ID {list1[2][1]} is Name :", list1[5][1] + " " + list1[8][1] + ",", f"Gender : {list1[11][1]}")
print(f"Details with us, for customer with cust ID {list1[2][2]} is Name :", list1[5][2] + " " + list1[8][2] + ",", f"Gender : {list1[11][2]}")
print(f"Details with us, for customer with cust ID {list1[2][3]} is Name :", list1[5][3] + " " + list1[8][3] + ",", f"Gender : {list1[11][3]}")