class Employee:
    company = "System Ltd"
    address = "Karachi"
    def show(self):
         print(f"The name is {self.name} and salary is {self.salary}")


# class Programmer:
#     company = "10 Pearl"
#     #~ I want same show class in this programmer class
#     def show(self):
#          print(f"The name is {self.name} and salary is {self.salary}")
#     def showLanguage(self):
#          print(f"Your Programming language is {self.language}")

#? Issue is if we copy and paste every class method then this will resulted in error and we can miss updation


#? I will use inheritance concept:
class Programmer(Employee):
    comapny = "10 Pearl"
    def showLanguage(self):
        print(f"Your Programming language is {self.language}")

#!Note: Employee is parent / Base class where as Programmer is inherited class

a = Employee()
b = Programmer()

# print(a.company , b.company)

# print(b.address)

#~Types of Inheritance
# Single Inheritance : Base - > Drived class
# Multiple Inheritance : Parent 1 & Parent 2 = > Child class 
# Multiple Level Inheritance

#~ Multi Inheritance example: 
# class Emp:
#     company = "System Ltd"
#     address = "Karachi"
#     def show(self):
#          print(f"The name is {self.name} and salary is {self.salary}")

# class kitchen:
#     kitchenName = "Abc"
#     def cookingFood(self):
#         print("You are cooking food")

# class Cooker(Emp and kitchen):
#     comapny = "10 Pearl"
#     def showLanguage(self):
#         print(f"Your Programming language is {self.language}")

# a = Cooker()

# print(a.kitchenName)
# print(a.comapny)

#~ Multi Level sInheritance example: 
class Emp:
    company = "System Ltd"
    address = "Karachi"
    def show(self):
         print(f"The name is {self.name} and salary is {self.salary}")

class kitchen(Emp):
    kitchenName = "Abc"
    def cookingFood(self):
        print("You are cooking food")

class Cooker(kitchen):
    comapny = "10 Pearl"
    def showLanguage(self):
        print(f"Your Programming language is {self.language}")

a = Cooker()

print(a.kitchenName)
print(a.comapny)





