class Dog(object):
    pass

    __instace = None

    # def __new__(cls, *args, **kwargs):
    #     if cls.__instace is None:
    #         cls.__instace = object.__new__(cls)
    #         return cls.__instace
    #     else:
    #         return cls.__instace

    def __new__(cls,name):
        if cls.__instace is None:
            cls.__instace = object.__new__(cls)
            return cls.__instace
        else:
            return cls.__instace

    def __init__(self,name):
        self.name = name

    def __str__(self):
        print("I am a animal , My name is %s"%(self.name))
        # print(self.name)


    def setName(self,name):
        self.name = name
        print(self.name)

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        # print("llaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        if not hasattr(cls, '_instance'):
            print("llaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def papappap(self):
        print("我要进行啪啪啪啪；啊")


if __name__ == "__main__":
    a = Dog("鸡")
    b = Dog("狗")
    c = Dog("猫")

    a.setName("鸡")
    b.setName("狗")
    c.setName("猫")

    print(id(a))
    print(id(b))
    print(id(c))

    print(a.__str__())
    print(b.__str__())
    print(c.__str__())

    # s1 = Singleton()
    # s2 = Singleton()
    # s1.papappap()
    # s2.papappap()
