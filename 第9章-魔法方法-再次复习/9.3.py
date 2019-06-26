class A:
    def Hello(self):
        print("Hello,I'm A")
class B(A):
    def Hello(self):
        print("Hello,I'm B")
    pass

a = A()
a.Hello()
b = B()
b.Hello()