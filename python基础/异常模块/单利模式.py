class Dog(object):
    pass

    __instace = None

    def __new__(cls, *args, **kwargs):
        if cls.__instace is None:
            cls.__instace = object.__new__(cls)
            return cls.__instace
        else:
            return cls.__instace


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
    a = Dog()
    b = Dog()
    c = Dog()

    print(id(a))
    print(id(b))
    print(id(c))

    # s1 = Singleton()
    # s2 = Singleton()
    # s1.papappap()
    # s2.papappap()
