class person:
    def __init__(self):
        self.name = "shanshan"
    def hello(self):
        print(self.name)
    def hello1(self):
        self.name = "shanshan1"
        print(self.name)
yanzhe = person()
yanzhe.hello()
yanzhe.hello1()
t  = person()
t.hello1()