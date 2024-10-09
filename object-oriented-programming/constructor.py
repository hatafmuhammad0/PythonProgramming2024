class Employee:
    language = "Python"
    salary = 1200000

    #~Dunder Method __init__ which is automatically call any method starts with "__" is Dunder method
    def __init__(self,language,salary) :
        self.language = language
        self.salary = salary
        print("I am an object")

    def getSalary (self): #! As this function use object data we need self here
        print (f"Salary of Employee is {self.salary}")
    
    @staticmethod
    def greeting(): #! As this function did not take object data here self is not needed we need to mark it as static mathod using @staticmethod 
        print("Good Morning")



#? We can also set instances using __init__
hataf = Employee("C++" , 1500000)
print(hataf.salary)