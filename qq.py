"""参数收集
"""
s = (1, 3, 4)


def test(*a):
    print(a)
    b, c, d = a
    return b

print(test(*s))
