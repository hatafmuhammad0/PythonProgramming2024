
#? Super method is used to access the methods of a super class in the derived class. call constructor of a base class in 

class Employee():
    def __init__(self):
        print("This is Employee Constructor")
    name = "default Name" 
    def EmployeeFunc(self):
        print(f"This is Employee from name {self.name}")

class Programmer():
    def __init__(self):
        print("This is Programmer Constructor")
    companyName = "System Ltd"
    def ProgrammerFunc(self):
        print(f"This is programmer from Company {self.companyName}")

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("This is Manager Constructor")
    ManagerName = "Hataf"
    def ManagerFunc(self):
        print(f"This is Manager from function {self.Manager}")

x = Manager()


