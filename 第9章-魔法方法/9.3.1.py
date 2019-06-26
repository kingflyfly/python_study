class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
r = Rectangle()
print(r.width)
r.width = 5
print(r.get_size())
print(r)