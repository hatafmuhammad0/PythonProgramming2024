
#! Write a program to print multiplication table of a given number for loop:

# table = int(input("Write a number for multiplication : "))

# for i in range(1,11):
#     print(f"{table} * {i} = {table*i}")

#! Write a program to greet all the person names stored in a list "l" and which starts with S.

# l = ["haris" , "sameer" , "link" , "seap" , "lion", "snake"]

# for i in l:
#     if(i.startswith("s")):
#         print(f"Welcome {i}")

#! Solve problem 1 with while loop

# i = 1
# table = int(input("Enter table number : "))

# while (i<11):
#     print(f"{table} x {i} : {table*i}")
#     i+=1

#! Write a program to find if the provided number is prime or not? 

"""1. Prime Number:
A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. In other words, a prime number is only divisible by 1 and the number itself."""

number = int(input("Enter a Number : "))

for i in range(2 , number):
    if(number % i )== 0 :
        print("Your number is not prime")
        break
    else:
        print("Your number is prime")
        break

