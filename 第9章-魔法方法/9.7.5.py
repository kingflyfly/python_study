#全局变量和局部变量
a = "test"
def test():
    global a
    c = a
    return c
b = test()
print(b)
print(a)