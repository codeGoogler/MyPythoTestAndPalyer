class MyCamera:
    pass

    def __init__(self):
        pass
        self.aa = 100

    num = 1;

    _num2 = 2

    # 这种 方式是调用不了的
    __num3 = 3

    def setNum3(self, newNum):
        self.__num3 = newNum
        print("我 调用了setNums方法")

    def getNum3(self):
        print("我 调用了getNums方法")
        return self.__num3

    myNun = property(getNum3, setNum3)

    # propety的第二种方法

    @property
    def mCount(self):
        return self.aa

    @mCount.setter
    def mCount(self,value):
        if isinstance(value,int):
            self.aa = value
        else:
            print("不是整数~~")

if __name__ == "__main__":
    pass
    myCamera = MyCamera()
    print(myCamera.num)
    print(myCamera._num2)
    print(myCamera.getNum3())
    print("*"* 50)
    myCamera.myNun = 100 # 其实是调用setNum3方法
    print(myCamera.myNun) # s其实是调用 getNun方法

    print("*"* 50)
    print("=============的第三种用法============")
    myCamera.mCount = 1024  # 其实是调用setNum3方法
    print(myCamera.mCount)