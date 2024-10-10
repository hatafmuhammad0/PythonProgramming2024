
#! This concept focuses on using reuseable code. (DRY Principle) 

#! class: A blueprint to create an object.
# Example : You need to fill an admission form , until the form is not fill up it is class and once it is filled by the person this will be an object of that person .

with open("object_orianted_programming.py") as o:
    content = o.read()


with open(f"object-oriented-programming/object-oriented.py","w") as no:
    no.write(content)