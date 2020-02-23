class Person(object):
    def __init__(self):
        self.a = 1
        self.b = 2
    def test(self):
        print(self.a)

class YanZhe(Person):
    def __init__(self):
        #使用未绑定方法调用父类的构造方法
        # Person.__init__(self)
        #通过super()函数调用父类的构造方法
        super(YanZhe,self).__init__()
        self.b = 3
    def test(self):
        print(self.b)
t = YanZhe()
t.test()
