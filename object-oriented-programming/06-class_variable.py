class Car:
    total_Car = 0
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
        Car.total_Car +=1
    def car_fullName(self):
        print(f"Car brand is {self.brand} and Model is {self.model}")


#! Creating a variable in Class and as an example for above check how many car is created using Car class?  

car1 = Car("Toyota","3004")
car2 = Car("Toyota","3004")
car5 = Car("Toyota","3004")
car6 = Car("Toyota","3004")
car10 = Car("Toyota","3004")
car11 = Car("Toyota","3004")

#! How to acess variable?
print(Car.total_Car)