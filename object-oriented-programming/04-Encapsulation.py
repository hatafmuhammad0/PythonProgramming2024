class Car:
    def __init__(self, brand,model):
        self.__brand = brand
        self.model = model
    #!We are creating a method to access brand. get is not a fixed name but convention is to use get to set a getter function
    
    def get__brand(self):
        print(f"Your brand is {self.__brand }")
    
    def car_fullName(self):
        print(f"Car brand is {self.__brand} and Model is {self.model}")

car1 = Car("Toyota","Safari")
car1.car_fullName() #We can Access brand here
#print(car1.__brand) #! Error as now we can't access it

#! Encapsulation concept => Modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# if we use __ before an atribute it will private it and to acess it we need a method as in above example we will private brand 