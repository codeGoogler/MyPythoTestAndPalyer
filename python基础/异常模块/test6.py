class Store(object):

	def select_car(self):
		pass

	def order(self, car_type):
		return self.select_car(car_type)

class BMWCarStore(Store):
	def select_car(self, car_type):
		return BMWFactory().select_car_by_type(car_type)

class BMWFactory(object):
	def select_car_by_type(self, car_type):
		pass
		# if car_type=="mini":
		# 	return Suonata()
		# elif car_type=="720li":
		# 	return Mingtu()
		# elif car_type=="x6":
		# 	return Ix35()

bmw_store = BMWCarStore()
bmw = bmw_store.order("720li")



class CarStore(Store):
	def select_car(self, car_type):
		return Factory().select_car_by_type(car_type)

class Factory(object):
	def select_car_by_type(self, car_type):
		if car_type=="索纳塔":
			return Suonata()
		elif car_type=="名图":
			return Mingtu()
		elif car_type=="ix35":
			return Ix35()

class Car(object):
	def move(self):
		print("车在移动....")
	def music(self):
		print("正在播放音乐....")
	def stop(self):
		print("车在停止....")

class Suonata(Car):
	pass

class Mingtu(Car):
	pass

class Ix35(Car):
	pass


def sssTest():
	car_store = CarStore()
	car = car_store.order("索纳塔")
	car.move()
	car.music()
	car.stop()


