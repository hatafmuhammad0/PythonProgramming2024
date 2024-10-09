
#? Create a class "Programmer" for storing information of few programmers working at Microsoft.

# class Programmer:
#     company = "Microsoft"
#     def __init__(self,name,salary,pincode):
#         self.name = name
#         self.salary = salary
#         self.pincode = pincode

# p = Programmer("Hataf",1200000,2445)

# print(p.name,p.company,p.salary,p.pincode)

#? Write a class "calculator" capable of finding square , cube and square root of a number

# class Calculator:
#     def __init__(self,number):
#         self.number = number
#     def square(self):
#         print(f"Square of {self.number} = {self.number**self.number}")
#     def cube(self):
#         print(f"cube of {self.number} = {self.number**3}")
#     def squareRoot(self):
#         print(f"Square root of {self.number} = {self.number**1/2}")
# num1 = Calculator(2)

# num1.square()
# num1.cube()

#! Write a class Train which has a method to book a ticket , get status (no seats) and get fare information of train running under railways
import random

class Train():
    def __init__(self,trainNo,fro,to):
        self.trainNo = trainNo 
        self.fro = fro 
        self.to = to 
    
    def bookTicket(self):
        print(f"You train is booked in train no. {self.trainNo} from {self.fro} to {self.to}")

    def getStatus(self):
        print(f"You train no. {self.trainNo} run sucessfully!")

    def fareInfo(self):
        print(f"You train ticket fare for train no. {self.trainNo} from {self.fro} to {self.to} is  ${random.randint(1,20)}")

train1 = Train(804,"Karachi","Islamabad")

train1.bookTicket()
train1.fareInfo()
train1.getStatus()