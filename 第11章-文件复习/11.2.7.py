a = [1,2,3,4]
b = a[:]
print(id(a))
print(id(b))
a = (1,2)
b = a[:]
print(id(a))
print(id(b))
print(type(a))
print(type(b))
a = "dsf"
b = a[:]
c = a
print(id(a))
print(id(b))
print(id(c))
print(type(a))
print(type(b))
