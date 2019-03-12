


class Animal:

    def __init__(self,name,weight,sex):
        self._name = name
        self._weight = weight
        self._sex = sex

    def __str__(self):
        return "出生了一个小孩：姓名：%s  ,性别：%s ,体重：%.2f千克"%(self._name,self._sex,self._weight)

    def eat(self):
        print("我是一只动物，我的名字是： %s，我的进行吃饭啦~"%(self.getName()))

    def setName(self, name):
        self._name = name

    def getName(self):
        return  self._name

    def setWeight(self, weight):
        self._weight = weight
    def getWeight(self):
        return  self._weight

    def setSex(self, sex):
        self._sex = sex
    def getSex(self):
        return  self._sex


# 不但能继承父类，而且还能继承父类的父类
class Dog(Animal):

    def shout(self):
        print("我是一只狗，名字叫做："+self.getName()+"，我的行为只会：汪汪汪！")

    def eat(self):
        # print("我是一只动物，我的名字是： %s，我的进行吃饭啦~"%(self.getName()))
        print("===================")


# eg

class 牧羊犬(Dog):

    def shout(self):
        print("我是一只狗，名字叫做："+self.getName()+"，我的行为只会：汪汪汪！")

    def eat(self):
        # print("我是一只动物，我的名字是： %s，我的进行吃饭啦~"%(self.getName()))
        print("===================")



class 采狗(Dog):

    def shout(self):
        print("我是一只狗，名字叫做："+self.getName()+"，我的行为只会：汪汪汪！")

    def eat(self):
        # print("我是一只动物，我的名字是： %s，我的进行吃饭啦~"%(self.getName()))
        print("===================")

        # 重写父类第一种方式
        Dog.eat(self)

        #重写父类第二种方式
        super().eat()


if __name__ == "__main__":
    pass
    print("*" * 90)
    baby = Animal("",0,"")
    baby.setName("李静波")
    baby.setWeight(51.5)
    baby.setSex("男")
    # print(baby.__str__())

    baby2 = Dog("",0,"")
    baby2.setName("史海波")
    baby2.setWeight(52.5)
    baby2.setSex("男")
    baby2.shout()
    baby2.eat()

    黑虎 = 牧羊犬("",0,"")
    黑虎.setName("曹斌")
    黑虎.setWeight(52.5)
    黑虎.setSex("男")
    黑虎.shout()
    黑虎.eat()

    小采狗 = 采狗("",0,"")
    小采狗.setName("大妹子")
    小采狗.setWeight(52.5)
    小采狗.setSex("男")
    小采狗.shout()
    小采狗.eat()



    # print(baby.__str__())
    # print(baby2.__str__())