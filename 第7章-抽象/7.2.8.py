class Person(object):
    def p(self,name):
        print('开始绘图')
        name.user(self)

class Name(object):
    def user(self,person):
        print(33333333333333333333)
        print(self)
        print(person)

p = Person()
p.p(Name())

