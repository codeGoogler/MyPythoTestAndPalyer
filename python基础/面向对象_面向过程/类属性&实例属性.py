


# 实例属性：和某个具体的实例对象有关系，并且一个实例对象和另外一个实例对象之间不进行共享
# 类 属 性：类属性属于它的类对象，并且多个实例对象之间，共享一个实例属性



class Toos(object):
    pass

    # 类属性
    num = 0;

    # 实例方法
    def __init__(self, name):
        pass
        # 实例属性
        self.name = name;
        Toos.num +=1


if __name__ == "__main__":
    pass
    t1 = Toos("张三")
    print("t1=%d"%t1.num)
    t2 = Toos("张三")
    print("t2=%d"%t2.num)
    t3 = Toos("张三")
    print("t3=%d"%t3.num)
    print("Toos=%d"%Toos.num)
