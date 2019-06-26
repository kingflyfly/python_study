a = [[1,2],[3],[4],[5],[6,7]]
def flatern(net):
    for i in net:
        for ii in i:
            yield ii
for i in flatern(a):
    print(i)
print(list(flatern(a)))

