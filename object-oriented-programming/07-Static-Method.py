class Car:
    total_Car = 0
    def __init__(self, brand,model):
        self.__brand = brand
        self.model = model
        Car.total_Car +=1
    def car_fullName(self):
        print(f"Car brand is {self.__brand} and Model is {self.model}")
    
    @staticmethod
    def greeting():
        print("Welcome to Show room!!!!")

    @property
    def brand(self):
        return self.__brand

car1 = Car("z","z")




