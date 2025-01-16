g = 12
h = 12
print("g is h : ", g is h)
print("id(g) : ", id(g))
print("id(h) : ", id(h))

a = 4
b ='4'
print("a is b : ", a is b)
print("id(a) : ", id(a))
print("id(b) : ", id(b))
print()

x = 24
print("id(x) : ", id(x))
x = 19
print("id(x) which got overwritten : ", id(x))
print()

p = 7
q = 7.0
print("p is q : ", p is q)
print("id(p) : ", id(p))
print("id(q) : ", id(q))
print()

o = 3
print("id(o) : ", id(o))
o = 8
print("o is o : ", o is o) # next o will overwrite the previous o value
print("id(o) : ", id(o))
print("id(o) : ", id(o))