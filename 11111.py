class person:
    yanzhe = ["name","age","sex"]
    shanshan = ["name","age","sex"]
    def p(self):
        print(self.yanzhe)

a = person()
person.yanzhe = ['name']
a.p()
