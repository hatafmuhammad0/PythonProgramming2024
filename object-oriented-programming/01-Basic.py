
#! create a Car class with attribute like brand and model. Then create instance of this class.

# class Car:
#     brand = None
#     model = None


# car1 = Car()
# car2 = Car()

# car1.brand , car1.model = {"Toyota" , "2024"}
# print(car1.brand)

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota",2024)
print(car1.model)
