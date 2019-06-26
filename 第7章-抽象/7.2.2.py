class Person:
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def greeting(self):
        print("hello,world! I.m{}.".format(self.name))
