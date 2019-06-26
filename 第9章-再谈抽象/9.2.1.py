class A:
    def hello(self):
        print("hello,I'm A")
class B(A):
    pass

a = A()
b = B()
a.hello()
b.hello()

class B(A):
    def hello(self):
        print("Hello, I'm B.")
b = B()
print(b.hello())

class A:
    def hello(self):
        print("hello,I'm A")
class B:
    def hello(self):
        print("Hello,I'm B")
b = B()
b.hello()

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("Ahhhhhh:")
            self.hungry = False
        else:
            print("no,thinks")
class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = "kakakaka"
    def sing(self):
        print(self.sound)
sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
