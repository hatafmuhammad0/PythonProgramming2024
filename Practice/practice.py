
#! Create a class (2-D) and use it to create another class represnting a 3-D vector 

# class TwoDVector:
#     def __init__(self,i,j):
#         self.i = i 
#         self.j = j

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")

# class ThreeDVector(TwoDVector):
    
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k
    
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j+ {self.k}k ")

# a = TwoDVector(1,2)

# a.show()

# b = ThreeDVector(1,2,3)

# b.show()

#! create a class "Pets" from a class "Animals" and further create a class "Dog" from "Pets". Add method "bark" to class dog

# class Animal:
#     def __init__(self,animalName):
#         self.animalName = animalName

# class Pets(Animal):
#     def __init__(self,petName, animalName):
#         super().__init__(animalName)

# class dog(Pets):
#     @staticmethod
#     def bark():
#         print("Woo Woo")

# d = dog("a","b")
# d.bark()

#!  Create a class "Employee" and add salary and increment properties to it.

class Employee:
    def salary(self,salary):
        return salary

    def increment(self,salary,increment):
        print(f"You current salary is {salary} and increment by {increment}% = {salary* (1+ (increment/100))}")

x = Employee()

x.salary = 100
print(x.salary)