class Person:
    def sayhello(self):
        print("hello!")
#        return 10
t = Person()
t.sayhello()
#print(t)

class Mystring:
    str = "yanzhe"
    def output(self):
        print(self.str)
s = Mystring()
s.output()

class Mystring:
    def __init__(self):
        self.str = "yanzhe"
    def output(self):
        print(self.str)
s = Mystring()
s.output()

class Ueserinfo:
    def __init__(self,name,pa):
        self.username = name
        self.passpord = pa
    def output(self):
        print("yonghu:",self.username ,"\nmima:",self.passpord)
s = Ueserinfo("yanzhe","123456")
s.output()
print("\n")
