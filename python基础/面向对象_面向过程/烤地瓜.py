

class Kdg:
    def __init__(self,cookedLevel,cookeString,condiments):
        pass
        self.cookedLevel = cookedLevel
        self.cookeString = cookeString
        self.condiments = condiments


    def __str__(self):
        return self.condiments,self.condiments,self.condiments


    def cook(self):
        print("地瓜描述：%s, 需要的配料：%s  ,需要把地瓜烤成%d分熟悉"%(self.cookeString,self.condiments,self.cookedLevel))
        print("开始烤地瓜啦:要烤地瓜的描述：%s"%self.cookeString)

    def addCoodiments(self):
        print("给地瓜添加配料:%s"%self.condiments)





if __name__ == "__main__":
    cook = Kdg(8,"考得非常好，已经熟透啦","添加了番茄酱和芝麻粉")
    cook.cook()
    cook.addCoodiments()