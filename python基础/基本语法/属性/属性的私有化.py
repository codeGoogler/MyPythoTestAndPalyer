class MyCamera:
    pass

    def __init__(self):
        pass

    num = 1;

    _num2 = 2

    # 这种 方式是调用不了的
    __num3 = 3

    def setNum3(self, newNum):
        self.__num3 = newNum

    def getNum3(self):
        return self.__num3


if __name__ == "__main__":
    pass
    myCamera = MyCamera()
    print(myCamera.num)
    print(myCamera._num2)
    print(myCamera.getNum3())
