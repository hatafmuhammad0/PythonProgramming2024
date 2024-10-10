class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
    def car_fullName(self):
        print(f"Car brand is {self.brand} and Model is {self.model}")

car1 = Car("Toyota","2008")

car1.car_fullName()