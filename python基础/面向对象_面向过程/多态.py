

class MyObject(object):
    pass
    def eat(self):
        pass

    def takeClothse(self):
        pass

    def live(self):
        pass

    def live(self):
        pass



class Animal(MyObject):


    def __str__(self):
        pass

    def __del__(self):
        pass #销毁的方法

    def eat(self):
        print("Animal eat")

    def grow(self):
       print("Animal grow")


class Plant(MyObject):

    def grow(self):
        print("Plant grow")

    def eat(self):
        print("Plant  eat")



def printObjectGrow(M):
        M.grow()


if __name__ == "__main__":
    pass
    amimal = Animal()
    amimal.eat()

    plant = Plant()
    plant.grow()

    printObjectGrow(amimal)
    printObjectGrow(plant)

