class Foobar:
    def __init__(self):
        self.name =42
f = Foobar()
print(f.name)

class Foobar:
    def __init__(self,value=43):
        self.somevalue = value
f1 = Foobar()
print(f1.somevalue)
f2 = Foobar("hello,world!")
print(f2.somevalue)

