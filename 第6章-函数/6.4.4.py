def print_params(*parms):
    print (parms)
print_params("testing")
print_params("testing","teing","te")

def print_params_2(title,*parms):
    print (title)
    print (parms)
print_params_2("parrmgs",1,2,3,45,"df")
print_params_2("1")
def in_the_middel(x,*y,z):
    return (x,y,z)
print(in_the_middel(1,2,3,4,5,6,7,z=8))

def print_params_3(**params):
    print(params)
print(print_params_3(x=1,y=2,z=3))

def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)
print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
