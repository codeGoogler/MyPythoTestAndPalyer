
class CarSotre(object):
     def order(self,price):
         if 5000 < price < 10000:
             return Car()


class CarO(object):

    def move(self):
        print(" I am a car ,I am moving")

    def runing(self):
        print(" I am a car ,I am runing")

    def stop(self):
        print(" I am a car ,I am stop")

    def relax(self):
        print(" I am a car ,I am relax")

class Car(CarO):

    def move(self):
        print(" I am a car ,I am moving")

    def runing(self):
        print(" I am a car ,I am runing")

    def stop(self):
        print(" I am a car ,I am stop")

    def relax(self):
        print(" I am a car ,I am relax")



if __name__ == "__main__":
    carStore =  CarSotre()
    car = carStore.order(9000)
    car.move()
    car.runing()
    car.stop()
    car.relax()