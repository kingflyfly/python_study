class Bird():
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("hahhah")
            self.hungry = False
        else:
            print("no,thinks")
class singsong(Bird):
    def __init__(self):
        super().__init__()
        #Bird.__init__(self)
        self.sound = "sw"
    def sing(self):
        print(self.sound)
b = Bird()
b.eat()
c = singsong()
c.eat()
c.eat()
c.sing()