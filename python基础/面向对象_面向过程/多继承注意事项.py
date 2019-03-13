

class Animal(object):


    def __str__(self):
        pass

    def __del__(self):
        pass #销毁的方法

    def eat(self):
        print("eat")


class Plant(object):
    def grow(self):
        print("grow")



class Something (Animal,Plant):
    def papapa(self):
        print("papappa")


    def eat(self):
        print("eat")
        Animal.eat(self)

        super().eat();

if __name__ == "__main__":
    aminal = Animal()
    aminal.eat()

    plant = Plant()
    plant.grow()

    somethinf = Something()
    somethinf.papapa()
    somethinf.eat()

    # 用于打印调用父类的顺序
    print(Something.__mro__)