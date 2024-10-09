
#! Class Method
# A Class method is a method which is bound to the class and not the object of the class 

class Employee:
    a = 1
    @classmethod
    def func(cls):
        print(f"The class attribute is {cls.a}")


x = Employee()
x.func()

x.a = 45 #Due to this class attribute is over power by instance attribute 
x.func() #now due to class method decorator class over power object

#~ I need to keep the class attribute as it is even if instance attribute want to change it we need to use class method decorator 