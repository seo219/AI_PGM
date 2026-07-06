class Car:
    def __init__(self, make, color, price):
        self.make = make
        self.color = color
        self.price = price

    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price

    def set_make(self, make):
        self.make = make
    def get_make(self):
        return self.make

    def __str__(self):
        return f"Car(make={self.make}, color={self.color}, price={self.price})"

class ElectricCar(Car) :
	def __init__(self, make, model, color, price, batterySize):
		super().__init__(make, color, price)
		self.model = model
		self.batterySize=batterySize
	def setBatterySize(self,  batterySize):
		self.batterySize=batterySize

	def getBatterySize(self):
		return self.batterySize

myCar = ElectricCar("Tesla", "Model S", "Red", 80000, 100)
print(myCar)

