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

# 3.
x = 24
print("id(x) : ", id(x))
x = 19
print("id(x) which got overwritten : ", id(x))
"""
OUTPUT -
id(x) :  1832069262352
id(x) which got overwritten :  1832069262192
"""

# 4.
p = 7
q = 7.0
print("p is q : ", p is q)
print("id(p) : ", id(p))
print("id(q) : ", id(q))
"""
OUTPUT -
p is q :  False
id(p) :  1832069261808
id(q) :  1832071769104
"""

# 5.
o = 3
print("id(o) : ", id(o))
o = 8
print("o is o : ", o is o) # next o will overwrite the previous o value
print("id(o) : ", id(o))
print("id(o) : ", id(o))
