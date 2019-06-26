a = [[1,2],[3],[[4,5],[6],[7,[8,9]]]]
def faltern(net):
    try:
        for i in net:
            for ii in faltern(i):
                yield ii
    except TypeError:
        yield net
print(list(faltern(a)))
