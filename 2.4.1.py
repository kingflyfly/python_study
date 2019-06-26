b = [1]
#c = []
a = ["asdf",2,"dsfsd","sdsf"]
print(a)
print(len(a))
a.append("syanzhe")
print(a)
a.insert(1,"shanshan")
print(a)
a.extend(b)
print(a)
c = a + b
print(c)
del c[0]
print(c)
print(c.index(2))
for var in c:
    print(var)