class Employee:
    language = "python" #! class attribute
    age = 32

hataf = Employee()
print(hataf.language) 
hataf.language = "JS" #! instance attribute
print(hataf.language)

#! Note : instance attributes takes prference over class attribute during assignment & retrivel 


