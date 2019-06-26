class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

st =Student("yanzhe","99")
print (st.name)
print (st.score)


class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age


obj1 = Foo('wupeiqi', 18)
print (obj1.name)  # 直接调用obj1对象的name属性
print (obj1.age)  # 直接调用obj1对象的age属性

obj2 = Foo('alex', 73)
print (obj2.name)  # 直接调用obj2对象的name属性
print (obj2.age)  # 直接调用obj2对象的age属性


class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print
        self.name
        print
        self.age
obj1 = Foo('wupeiqi', 18)
print (obj1.detail(name))