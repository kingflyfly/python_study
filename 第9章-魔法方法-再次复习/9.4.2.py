class Person:
    def __init__(self):
        self.__name = None
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def delName(self):
        del self.__name
    name_value = property(getName,setName,delName)

p = Person()
#p.name_value = "yanzhe"
p.setName("shanshan")
#n = p.name_value
print(p.getName())
#print(n)
#del p.name_value
#print(p.name_value)