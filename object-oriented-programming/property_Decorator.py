# class Employee:
#     a = 1
#     @classmethod
#     def func(cls):
#         print(f"The class attribute is {cls.a}")
    
#     @property
#     def name(self):
#         return self.name
    
#     @name.setter
#     def name(self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]
#         print(f" First name is {self.fname} and Last name is {self.lname}")
    
# e = Employee()
#~ I want to set a property in Employee directly
# e.name = "Muhammad Hataf"

#~ The above concept is abstraction (User don't know the detail of components working behind the scenes)  and Incapsulation (Different working components are pack in one class )

#~ If there is a method in a class which you want to declear it as property 
#~ It allow you to acess that method as attribute
#~ @Property is used to define a getter method that can be accessed like an attribute.
#~ @radius.setter -> it allows the radius to be modified with validation.

#! Example 1 : Timing execution Function
# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()        
#         print(f"{func.__name__} ran in {end-start} ")
#         return result
#     return wrapper

# @timer
# def example_func(n):
#     time.sleep(n)

# example_func(2)
#! Example 2 : Debugging Function Calls

# def Debugging(func):
#     def checker(*args, **kwargs):
#         func(*args, **kwargs)
#         print(f"{func.__name__} and arguemtns are {args} , {kwargs} ")
#         return func
#     return checker

# @Debugging
# def greet(name, greeting = "Hello"):
#     print(f"{greeting} , {name}")

# greet("hataf",greeting="Bye")


#! Example 3 : Cache Return Values

