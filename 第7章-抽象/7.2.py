class Person:
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.get_name
    def greet(self):
        print("hello,world!,Im's {}.".format(self.name))

foo = Person()
bar = Person()
foo.set_name('yanzhe')
#foo.get_name()
bar.set_name('shanshan')
foo.greet()
bar.greet()
    