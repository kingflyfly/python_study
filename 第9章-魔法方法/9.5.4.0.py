class Ren():
    def __init__(self):
        self.width = 0
    def __getattr__(self, sdf):
        if sdf == 'yanzhe':
            return 3
        else:
            raise AttributeError
p = Ren()
print(p.width)
print(p.yanzh1e)
print(p.__dict__)