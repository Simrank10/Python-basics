# 1.
x = 10
print("x = ", x)
"""
OUTPUT -
x =  10
"""

# 2.
x = x + 8
print("x + 8 = ", x)
"""
OUTPUT -
x + 8 =  18
"""

# 3.
x = 10
print("x = ", x)
"""
OUTPUT -
x =  10
"""

# 4.
x += 8
print("x += 8: ", x)
"""
OUTPUT -
x += 8:  18
"""

# 5.
p, q, r = 5, 3, 7
s = p + q + r
q -= 2
s *= q + p
print("s = ", s)

# s *= q + p
# The addition (q + p) is grouped together first, then the multiplication happens. 
# It does not mean s = s * q + p. Instead, it means s = s * (q + p)

"""
OUTPUT -
s =  90
"""
