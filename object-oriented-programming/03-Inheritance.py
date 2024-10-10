class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
    def car_fullName(self):
        print(f"Car brand is {self.brand} and Model is {self.model}")

#! Inherit from Car class
#! super keyword get access of parent class
class ElectricCar(Car):
    def __init__(self,brand, model ,batterySize):
        super().__init__(brand,model)
        self.battrysize = batterySize

car1 = ElectricCar("Tesla","JTK","240KW")

print(car1.model)
print(car1.battrysize)