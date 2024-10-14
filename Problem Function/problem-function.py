
#! Function with multiple parameter 

# def sumNum(a,b):
#     return a+b 

# print(sumNum(2,3))

#! Function multiply which multiply not only numbers but also string 

# def multiply(a,b):
#     return a*b

# print(multiply(2,"a"))

#! Function returing multiple values (area , circumfarence) of a circle given its radius.
# import math

# def CircleInfo(radius):
#     circumfarence = round((2*math.pi*radius),2)
#     area = round((math.pi*radius**2),2)
#     return (circumfarence,area)

# c,a = CircleInfo(3)
# print(f"Circumfarence = {c} and Area = {a}")

#! Default parameter in a function : Greet a user and if user name not provided use default name

# def greeting(name = "Sir"):
#     print(f"Welcome {name}")

# greeting()

#! Lamda Function => function to compute the cube of a number 
#~ Lamda mostly use in frameworks and Lamda is used only once
# cube = lambda x: x**3

# print(cube(3))

#! Function with *args
#~ Write a function that takes variable number of arguemnts and return their sum.

# def sumNum(*args):
#     # return sum(args) #! if we give args only it will be tuple but if *args is there it will be numbers
#     print(*args)
#     print(f"args = {args}")
#     print(sum(args))
#     print(sum(*args))
#     # print(f"Sum of varibale arguments is {sum(args)}")

# # print(sumNum(2,3,4,5))
# sumNum(2,3,4,5)

#! Function with **Kwargs => Function which accepts any number of keyword arguments and prints them in the format key : value

# def Kvalue(**kwarg):
#     for key,value in kwarg.items():
#         print(key,value)

# Kvalue(name= "Hataf" , Education = "ACCA")  

#! Generate a function with yield



