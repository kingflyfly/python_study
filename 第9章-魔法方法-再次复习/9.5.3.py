class Myclass:
    @staticmethod
    def smeth():
        print("this is a static method!")
    @classmethod
    def cmeth(cls):
        print("this is a class method of",cls)
Myclass.smeth()
Myclass.cmeth()