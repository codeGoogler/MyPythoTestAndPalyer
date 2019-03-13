class CarSotre(object):
    def __init__(self):
        self.factory = Foctory()

    def order(self, price):
        return self.factory.createCarByType(price)


class CarO(object):

    def move(self):
        print("CarO  I am a car ,I am moving")

    def runing(self):
        print("CarO I am a car ,I am runing")

    def stop(self):
        print("CarO I am a car ,I am stop")

    def relax(self):
        print("CarO I am a car ,I am relax")


class Car(CarO):

    def move(self):
        print(" Car I am a car ,I am moving")

    def runing(self):
        print("Car I am a car ,I am runing")

    def stop(self):
        print(" Car I am a car ,I am stop")

    def relax(self):
        print("Car  I am a car ,I am relax")


class AidiA8(CarO):
    pass

    def move(self):
        print(" AidiA8 I am a car ,I am moving")

    def runing(self):
        print("AidiA8 I am a car ,I am runing")

    def stop(self):
        print(" AidiA8 I am a car ,I am stop")

    def relax(self):
        print("AidiA8  I am a car ,I am relax")


class Foctory(object):
    def createCarByType(carType):
        if carType == 100:
            return CarO()
        elif carType == 102:
            return AidiA8()
        else:
            return Car()


if __name__ == "__main__":
    carStore = CarSotre()
    car = carStore.order(102)
    car.move()
    car.runing()
    car.stop()
    car.relax()
