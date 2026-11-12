a = (2, 10, 1991)
b = (25, 12, 1990)
c = ("Donald", True, b)
x, y = ((27, 3), 9)
z, w = x
v = (x, a)

print(a < b)
print(y + w)
print(x + a)
print(len(v))
print(v[1][1])
print(c[0][0])
print(z, y)
print(a + b[1:5])
print((a + b)[1:51])
print(str(a[2]) + str(b[2]))
print(str(a[2] + b[2]))
print(str((a + b)[2]))
print(str(a + b)[2])

dias_mes = [31, 28, 31, 30,
31, 30, 31, 31,
30, 31, 30, 31]