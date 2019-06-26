class Rectangle:
    def __init__(self):
        self.width = 0
        self.heigth = 0
    def set_size(self,size):
        self.width,self.heigth = size
    def get_size(self):
        return self.width,self.heigth
    size = property(get_size,set_size)

r = Rectangle()
print(r.heigth)
print(r.size)
r.size = 150, 100
print(r.width)
#print(r.get_size())
#r.set_size((150,100))
#print(r.get_size())
#print(r.get_size())