
#! This concept focuses on using reuseable code. (DRY Principle) 

#! class: A blueprint to create an object.
# Example : You need to fill an admission form , until the form is not fill up it is class and once it is filled by the person this will be an object of that person .

# class employee:
#     name = "hataf"
#     age  = 32


# hataf = employee()
# print(hataf.age , hataf.name)

#! Modelling A Problem in OOPS
#Noun -> Class -> Employee
#Adjective -> Attributes -> name , age , salary
#verbs -> Methods -> getSalary() , increment()

# hataf.language = "Python" #! This lanuage is object/instance attribute
# print(hataf.language)

#! in above case -> name and age is class attribute where as language is object/instance attribute as they directly belong to object

#? Self Parameter 

#? Class Method: A class method is bound to the class and not the object to the class. @class Method is used 

#! Example: 

# class Employee():
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"value of a is {cls.a}")

# e = Employee()
# e.show()
# e.a =45
# e.show()

#! Property Decorators => 
import math

class Circle:
    def __init__(self,radius):
        self._radius = radius #can not access _radius outside class

    @property                   #getter method
    def radius(self):
        return self._radius
    
    @radius.setter          #setter method
    def radius(self,value):
        if value<0:
            raise ValueError("Radius can not be negative")
        self._radius = value

    def area(self):
        return math.pi*self._radius


x = Circle(10)
print(x._radius) #access radius as attribute 

print(x.area()) #access area as property 

x.radius = 100 #update radius as an attribute using setter 

print(x.area())

