
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

# number = int(input("Enter a Number : "))

# for i in range(2 , number):
#     if(number % i )== 0 :
#         print("Your number is not prime")
#         break
#     else:
#         print("Your number is prime")
#         break

#Write a program to find sum of first n natural numbers using while loop

'''A natural number is any positive integer starting from 1 and continuing indefinitely. Natural numbers are the numbers we use for counting.'''

# n = int(input("Enter first n natural numbers : "))

# for i in range(1,n+1):
#     i += i 
#     print(f"{i}")

# n = int(input("Enter first n natural numbers : "))

# i = 0
# while (i<=n):
#     print(f"Sum of {n} Natural numbers are : {i}")
#     i += i  

#! Factorial of a given number 
'''3. Factorial:
The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. It is denoted as n!. The factorial of 0 is defined to be 1.

Example:
5! (read as "5 factorial") is 5 × 4 × 3 × 2 × 1 = 120.
3! is 3 × 2 × 1 = 6.
0! is defined to be 1.'''

# factorialNumber = int(input("Write a factorial number : "))
# x=1
# for i in range(1 , factorialNumber+1):
#     x = x * i
#     print(f"Factorial is  = {x}")

#! Write a program to print the following *** pattern

'''
  *
 ***
***** for n = 3 numbers'''



# n = int(input("Enter n : "))
# for i in range (1 , n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1), end="")
#     print("")

#! Write a program to print star pattern 

'''
*
**
***
'''

# n = int(input("Enter n number : "))
# for i in range(1, n+1):
#     print("*" * (i))

#! Write a program to print following patter 

'''
***
* *
*** for n = 3
'''

# n = int(input("Enter n numbers : "))

# for i in range(1,n+1):
#     if i == 2 and n % 2 == 0 :
#         print("*" *((n//2)-1),end="")
#         print(" " * 1,end="")
#         print("*"*((n//2)-1),end="")
#         print("")
#     elif i == 2 and n % 2 != 0 :
#         print("*"*(n//2),end="")
#         print(" " * 2,end="")
#         print("*"*(n//2),end="")
#         print("")
#     elif i == 1 or i == 3:
#         print("*"*n)

# for i in range (1, n+1):
#     if i == 1 or i == n :
#         print("*" * n)
#     else:
#         print("*",end="")
#         print(" " * (n-2),end="")
#         print("*",end="")
#         print("")

#! Write a multiplication table using for loop in reverse order 

# table = int(input("Enter table number : "))
# for i in range(1 , 11):
#     print(f"{table} x {11 - i} = {(table) * (11 - i)}" )