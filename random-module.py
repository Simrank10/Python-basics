import random

a = random.randint(12, 78)
print(a)

b = random.randint(2, 5)
print(b)

c = random.randrange(12, 78)
print(c)

d = random.randrange(2, 3)
print(d)

e = random.random()
print(e)

f = random.uniform(2, 5)
print(f)

lst = ["Cherry", 56.7, "Kite", 90000, 0.0422, False, True]
g = random.choice(lst)
print(g)

random.shuffle(lst)
print(lst)