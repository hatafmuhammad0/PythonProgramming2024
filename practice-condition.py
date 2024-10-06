
#! Write a program to find the greatest of four numbers entered by the user.

# num1 = input("Enter number : ")
# num2 = input("Enter number : ")
# num3 = input("Enter number : ")
# num4 = input("Enter number : ")

# if(num1>num2 and num1 > num3 and num1>num4):
#     print(f"Greater number is {num1}")
# elif(num2>num3 and num2>num4 and num3>num1):
#     print(f"Greater number is {num2}")
# elif(num3>num1 and num3>num2 and num3>num4):
#     print(f"Greater number is {num3}")
# else:
#     print(f"Greater Number is {num4}")

#! Write a program to find out whether a student has passed or failed if it requires a total 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

# mark1 = int(input("Enter Subject 1 marks : "))
# mark2 = int(input("Enter Subject 2 marks : "))
# mark3 = int(input("Enter Subject 3 marks : "))

# total_Percentage = 100*((mark1+mark2+mark3)/300)


# if(mark1/100 >= 0.33 and mark2/100 >= 0.33 and mark3/100 >= 0.33 and total_Percentage > 0.4 ):
#     print(f"You are passed , Your Percentage is {total_Percentage}")
# else:
#     print(f"You are failed, Your Percentage is {total_Percentage}")

#! A spam comments is defined as text containing following keywords: (Make alot of money , Buy now , click here , click this ) , write a program to detect these spams. 

# p1 = "Make alot of money"  
# p2 = "Buy now" 
# p3 = "click here"
# p4 = "click this"

# message = input("Enter your comments : ")

# if(p1 in message.lower() or p2 in message.lower() or p3 in message.lower() or p4 in message.lower()):
#     print("Your message contain spam")
# else:
#     print("Your message is clear")

#! Write a program to find whether a given username contain less than 10 character or not? 

# userName = input("Write your user Name : ")

# if(len(userName)<10):
#     print("Your user name contain less than 10 charater ")
# else:
#     print("Your user name is good to go ")

#! Write a program to find out whether a give name is in a list or not? 

# userName = input("Write user name here : ")

# userNameList = ["zksync" , "hataf" , "lion", "go"]

# if(userName in userNameList):
#     print(f"{userName} is in the list ")
# else:
#     print(f"{userName} not found in the list")

#! Write a program to calculate the grade of a student from his marks from the following scheme :
#! 90 - 100 => Excellent 
#! 80 - 90 => A 
#! 70 -80 => B
#! 60 - 70 => C 
#! 50 - 60 => D 
#! < 50 => Fail

# marks = int(input("Write your marks : "))

# if(marks < 50):
#     print("You are Fail")
# elif(marks>= 50 and marks<= 60):
#     print("Your Grade is D")
# elif(marks>= 60 and marks<= 70):
#     print("Your Grade is C")
# elif(marks>= 70 and marks<= 80):
#     print("Your Grade is B")
# elif(marks>= 80 and marks<= 90):
#     print("Your Grade is A")
# else:
#     print("Excellent ")



