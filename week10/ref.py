a = [1,2,3]
b = [1,2,3]

print(a == b)

b[2] = 4

print(a == b)

c = a

print(a == c)

c[2] = 100
print(c)
print(a)
