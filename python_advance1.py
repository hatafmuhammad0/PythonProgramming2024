
#? using walrus operator ":" we can define variable in same line

# if (n := len([2,3,4,5,6,7])) > 5: #! Here n is define and compare at the same time using ":" 
#     print("OK") 
# else:
#     print("Not OK")

#? TYPES operator 
# types hints are added using the colon(:) syntax or variables and the -> syntax for function return types.

# n : int = 5
# x : str = "hataf"


# a= int(input("Enter a number : "))
# b= int(input("Enter b number : "))
# def sum(a : int,b : int )-> int:
#     return (a+b)

# print(sum(a,b))

#? importing other data types to use : List , Tuple , Dict , union
# from typing import List,Union,Tuple
# #union means that the data can be a string or number

# x:list[int] = [2,3,4,5,6]
# a : Union[str,list,int] = [2,"sz"]

#? Exception handling 


    
# try: 
#     a = int(input("Enter : "))
#     print(a)
# except: #! This will not crash the program rather just show error and move forward
#     print("Na Na na error")

# print("thank u")

#? Raise error to developer :

# a = int(input("Enter a : "))
# b = int(input("Enter b : "))


# if(a == 0 or b ==0):
#     raise ZeroDivisionError("Hey our program input value is 0") #! program crash if error raise due to critical error 
# else:
#     print(a/b)

#? Try with else : we will go in else if except block not run or error not occured 

# try:
#     a = int(input("Enter number : "))
#     print(a)
# except:
#     print(f"Error occured please check")
# else:
#     print("I am in else")


#? try and finnaly => finally will run if try block or except block 
# why we use finally 

# try:
#     a = int(input("Enter number : "))
#     print(a)
# except:
#     print(f"Error occured please check")
# finally:
#     print("I am in finally block")

#? __name__ = "__main__" => if we are exporting a code and we dont want some code to run than we will write that code with if __name__ = "__main__" condition

# def greet():
#     print("Hello")



# if __name__ == "__main__":
#     greet()
#     print("We are directly running the code")

#? Enumerate 

# x = ["hataf","51","67"]

# for index, item in enumerate(x,1):
#     print(f"{index} = index and {item} = item")


#? list comprehension
l = [1,2,3,4,5]
squareList = [i*i for i in l]
print(squareList)





