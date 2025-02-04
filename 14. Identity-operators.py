# 1.
g = 12
h = 12
print("g is h : ", g is h)
print("id(g) : ", id(g))
print("id(h) : ", id(h))
"""
OUTPUT -
g is h :  True
id(g) :  1832069261968
id(h) :  1832069261968
"""

# 2.
a = 4
b ='4'
print("a is b : ", a is b)
print("id(a) : ", id(a))
print("id(b) : ", id(b))
"""
OUTPUT -
a is b :  False
id(a) :  1832069261712
id(b) :  1832074960688
"""

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
