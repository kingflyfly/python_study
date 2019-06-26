class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("Ahaaaa")
            self.hungry = False
        else:
            print("no,thanks")
class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = "songs"
    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()