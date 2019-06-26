def test(arg,*args):
    print(arg,args)
    print(sum(args))
test(1,2,3,4)

def test(arg,**args):
    print(arg,args)
test(1,a = 3,b =4,c = 5,d = 6)
print(sum([2,1]))