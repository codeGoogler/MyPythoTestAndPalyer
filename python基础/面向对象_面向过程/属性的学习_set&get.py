

class Persion:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return self.name ,self.age,self.sex


if __name__ == "__main__":
    pass

    p = Persion("张三",28,"男")

    print p.__str__()
