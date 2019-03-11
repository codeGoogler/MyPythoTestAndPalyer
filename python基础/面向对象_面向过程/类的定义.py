import self as self


class Animal:

        def __init__(self,name,age,color,wight):
            self.name = name
            self.age = age;
            self.color = color
            self.wight = wight
        def __str__(self):
            return self.name,self.age,self.wight,self.color


        def eat(self):
            print("进行吃的方法")

        def call(self):
            print("一个叫做%s，活了%d年的动物,其该动物的毛色为%s 进行叫的方法~~"%(self.name,self.age,self.color))




if __name__ == "__main__":

    # print("类的学习和创建")
    # dog = Animal()
    # dog.name = "黑虎子"
    # dog.age = 12
    # dog.color = "123"
    # dog.call()

    cat = Animal("猫",12,345,12.12)
    cat.name = "猫";
    cat.age = 12
    cat.color = 345
    cat.wight =12.38
    print(cat.__str__())