x = 1
print (x)
scope = vars()
scope['x']
scope['x'] += 1
print (x)
def foo():x = 2
x = 1
foo()
x
print (x)
def output(x):print (x)
x = 2
y = 5
output(y)
output(x)
x = "sdfsdf"
def huibing(h):print(h+x)
huibing("ninhao")
print

def combine(parameter):
    print(parameter + globals()['parameter'])
parameter = 'berry'
combine('Shrub')
x = 1
def change_globe():
    global x
    x += 1
change_globe()
print(x)
def foo():
    def bar():
    print("Hello, world!")
    bar()
