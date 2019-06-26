class Person:
    def __init__(self,num =4):
        self.a = num
    def __setattr__(self, name, value):
        self.__dict__[name] = value
r = Person(40)
print(r.__dict__)
r.tag = "yanzhe"
print(r.__dict__)
