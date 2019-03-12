import  sys


class Chirld:

    def __init__(self,name,weight,sex):
        self._name = name
        self._weight = weight
        self._sex = sex

    def __str__(self):
        return "出生了一个小孩：姓名：%s  ,性别：%s ,体重：%.2f千克"%(self._name,self._sex,self._weight)


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

    def __del__(self):
        print("我被删除啦")

if __name__ == "__main__":
    pass
    print("*" * 90)
    baby = Chirld("",0,"")
    baby.setName("李静波")
    baby.setWeight(51.5)
    baby.setSex("男")
    print(baby.__str__())
    print(sys.getrefcount(baby))
    baby2 = baby
    print(sys.getrefcount(baby))

    del  baby
    print(sys.getrefcount(baby))
    del  baby2
    print(sys.getrefcount(baby2))
    # print(baby.__str__())
    # print(baby2.__str__())