#迭代器
class test:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        return self.a
    def __iter__(self):
        return self
r = test()
print(next(r))
print(next(r))
print(next(r))

