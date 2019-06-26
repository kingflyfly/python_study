def add(x,y):
    return x + y
print (add(2,3))
par=(1,22)
print (add(*par))

def hello_3(greeting='Hello', name='world'):
    print('{}, {}!'.format(greeting, name))
par = {"name":"yan zhe","greeting":"well meet"}
print(hello_3(**par))

def with_stars(**kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')
args = {'name': 'Mr. Gumby', 'age': 42}
print(with_stars(**args))

