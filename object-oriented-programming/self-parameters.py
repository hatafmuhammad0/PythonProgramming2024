class Employee:
    language = "Python"
    salary = 1200000
    def getSalary (self): #! As this function use object data we need self here
        print (f"Salary of Employee is {self.salary} and language is {self.language}")
    
    @staticmethod
    def greeting(): #! As this function did not take object data here self is not needed we need to mark it as static mathod using @staticmethod 
        print("Good Morning")

hataf = Employee()

hataf.getSalary()
hataf.greeting()

#? Self refers to the instance of the class. It automatically passed with a function call from an object.

                    