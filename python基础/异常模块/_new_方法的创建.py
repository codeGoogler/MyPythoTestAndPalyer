class Animal(object):

    def __new__(cls, *args, **kwargs):
        print("__new__")
        # 这个哥们啊，返回一个常见对象的引用~~~~
        return object.__new__(cls)

    def __init__(self, name):
        print("init")
        self.name = name

    def __del__(self):
        print("__del__")

    def __str__(self):
        print("__str__")

    def papapa(self):
        print("我创建啦，要进行啪啪啪了~~~")

    def addNum(self):
        pass


class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


if __name__ == "__main__":

    # 下面的那个哥们相当于做了三件事情
    #  第一件事情，是 调用new方法创建对象，然后返回了一个变量来接收__new__的返回值，这个指标是创建出来的对象的引用
    #  __init__ 刚刚创建 出来的对象的应用·
    # 返回对象的引用
    #



    animal = Animal("臧三")
    animal.addNum()
    animal.papapa()
    animal2 = animal
    del  animal2
    animal.__str__()
    singletoin = Singleton()
