class Counterlist(list):
    def __init__(self,*args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.couter += 1
        return super(Counterlist, self).__getitem__(index)
cl = Counterlist(range(10))
print(cl)
cl.reverse()
print(cl)
del cl[3:6]
print(cl)
print(cl.counter)
cl[4] + cl[2]
cl.counter
