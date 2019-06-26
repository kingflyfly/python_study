import math
x = 1
y = math.sqrt
print(callable(x))
print(callable(y))

def hello(name):
    return "hello "+name+",welcome back!"
yanzhe = "yanzhe"
print(hello(yanzhe))