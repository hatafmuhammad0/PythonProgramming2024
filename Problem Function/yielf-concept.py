
#! yield = > Write a generator function that yields even numbers upto a specific limit.

# def evenNumGen(limit):
#     i = 0
#     x = []
#     while i<limit+1:
#         i+=1
#         if i%2==0:
#             x.append(i)
#         else:
#             continue
#     return x

# print(evenNumGen(10))

#! We are getting numbers in a list form and which we don't need , so we use yield

# def evenNumGen(limit):
#     i = 0
#     while i<limit+1:
#         i+=1
#         if i%2==0:
#             yield i
#         else:
#             continue
# for num in evenNumGen(10):
#     print(num)

#! Recursive function => Calculate the factorial of a number 

#~ This is non recursive
# def fact(number):
#     x = 1
#     for i in range (1,number):
#         x += (x* (number -i))
#     return x
# print(fact(3))

#~ This is recurssive

# def fact(number):
#     if number == 0 or number ==1:
#         return 1
#     return number * fact(number -1)

# print(fact(4))

#~ Write a recursive function to compute the n-th Fibonacci number. 

# def fib(n):
    
#     if n==0:
#         return 0
#     elif n == 1:
#         return 1
#     else: 
#         return fib(n-1) + fib(n-2)

# print(fib(6))

#~ Write a recursive function to find the sum of digits of a number. For example, the sum of digits of 1234 is 1 + 2 + 3 + 4 = 10.

# def sumNum(number):
#     if number == 0:
#         return 0
#     else:
#         return number + sumNum(number -1)

# print(sumNum(1234))

