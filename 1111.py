class myclass:
    def method(self):
        print( "instance method called:",self)
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    @staticmethod
    def staticmethod():
        return 'static method called'
my_class = myclass()
my_class.method()
my_class.classmethod()
