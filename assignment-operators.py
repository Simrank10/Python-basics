x = 10
print("x = ", x)
print()
x = x + 8
print("x + 8 = ", x)
print()

x = 10
print("x = ", x)
print()
x += 8
print("x += 8: ", x)
print()


p, q, r = 5, 3, 7
s = p + q + r
q -= 2
s *= q + p
print("s = ", s)
'''
s *= q + p
The addition (q + p) is grouped together first, then the multiplication happens. 
It does not mean s = s * q + p. Instead, it means s = s * (q + p)
'''

