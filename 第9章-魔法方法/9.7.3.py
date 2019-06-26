a  = [x * x for x in range(5)]
print(a)
a1 = (x * x for x in range(5))
print(type(a))
print(type(a1))
for x in a1:
    print(x)