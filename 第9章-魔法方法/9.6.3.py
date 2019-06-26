#判断变量a是否为字符串
a = (1,2)
try:
    a + ""
except TypeError:
    print(1)
else:
    print(2)