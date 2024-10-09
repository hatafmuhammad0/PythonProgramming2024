
#! This concept focuses on using reuseable code. (DRY Principle) 

#! class: A blueprint to create an object.
# Example : You need to fill an admission form , until the form is not fill up it is class and once it is filled by the person this will be an object of that person .

class employee:
    name = "hataf"
    age  = 32


hataf = employee()
print(hataf.age , hataf.name)

#! Modelling A Problem in OOPS
#Noun -> Class -> Employee
#Adjective -> Attributes -> name , age , salary
#verbs -> Methods -> getSalary() , increment()

hataf.language = "Python" #! This lanuage is object/instance attribute
print(hataf.language)

#! in above case -> name and age is class attribute where as language is object/instance attribute as they directly belong to object

#? Self Parameter 
