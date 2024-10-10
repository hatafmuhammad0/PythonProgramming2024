class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
    def car_fullName(self):
        print(f"Car brand is {self.brand} and Model is {self.model}")
    def fuel_Type(self):
        print("Fuel type is Petrol / Diseal")


class ElectricCar(Car):
    def __init__(self,brand, model ,batterySize):
        super().__init__(brand,model)
        self.battrysize = batterySize
    def fuel_Type(self):
        print("Fuel type is Charge")

#Same method but different result 
#Polymorphism example is fuel type for car and electric car is different 