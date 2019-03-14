class Tool(object):
    pass

    def __init__(self, numberNum):
        pass
        self.numberNum = numberNum

    # 我要定义一个梳理属性
    num = 0
    name = "张三"
    age = 14

    # 类方法
    @classmethod
    def showClassToos(cls):
        pass
        msg = "这个工具类里面总共又几口人：name :%s ,age :%d ,num :%d" % (cls.name, cls.age, cls.num)
        print(msg)

    # 静态方法
    @staticmethod
    def addAnotherPersionInfo():
        Tool.num = 100
        Tool.name = "李四"
        Tool.age = 21
        print("我调用了静态调度")

    # 实例方法
    def showPersion(self):
        print(self.num, self.name, self.age)

    def __str__(self):
        pass
        self.num = self.numberNum
        msg = "这个工具类里面总共又几口人：%d ,name :%s ,age :%d ,num :%d" % (self.numberNum, self.name, self.age, self.num)
        print(msg)


if __name__ == "__main__":
    pass
    tool = Tool(5)
    tool.__str__()

    # 类方法 既能通过类名.调用，又能通过实例对象来调用
    Tool.showClassToos()
    tool.showClassToos()

    # 静态方法 既能通过类名.调用，又能通过实例对象来调用
    Tool.addAnotherPersionInfo()
    tool.addAnotherPersionInfo()

    # 实例方法  通过实例对象来调用
    # Tool.showPersion() 这种写法是错误的
    tool.showPersion()

