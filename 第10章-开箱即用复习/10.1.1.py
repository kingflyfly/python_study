import json
a = [1,2,3]
a1 = (1,2,3)
b = json.dumps(a)
b1 = json.dumps(a1)
print(b)
print(type(b))
print(type(a))
print(b1)
print(type(b1))