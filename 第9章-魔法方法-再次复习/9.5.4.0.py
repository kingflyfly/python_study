class Ren():
    def __init__(self):
        self.width = 0
    def __getattr__(self, sdf):
        return 3
p = Ren()
print(p.width)
print(p.yanzhe)
print(p.__dict__)