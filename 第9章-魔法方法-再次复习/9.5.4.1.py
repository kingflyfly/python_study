class Ren(object):
    def __init__(self,heigth = 30):
        self.heigth = heigth
    def __setattr__(self, name, value):
        if name == "yanzhe":
            self.__dict__[name] = value

p = Ren()
p.yanzhe
