#Write function to find greatest of three numbers 

# def greatNum (a,b,c):
#     if a> b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     elif c > a and c > b:
#         print(c)

# greatNum(1,2,4)

#! Write a function to calculate the sum of first n natural numbers.

# def naturalNum (n):
#     if n == 1:
#         return 1
#     return naturalNum(n-1) + n 


# print(naturalNum(4))

#! Print a pattern using function 
'''
***
**
*
for (n = 3)
'''

# n = int(input("Enter Patter Range : "))
# for i in range (1 ,n):
#     print("*" * (n-i))

# def printPattern (n):
#     if(n == 0):
#         return 
#     print("*" * n)
#     printPattern(n-1)

# printPattern(n)

#! Write a program which converts inchs to cms

# def convertInchtoCm (inches):
#     print(f" {inches} inches in to Centimeter is : {inches * 2.54} cm.")

# convertInchtoCm(5)

#! Remove a word from a list 

def rem (li , word ):
    for item in li:
        li.remove(word)
        return li
    
li = ["Hataf" , "aj" , "ak","mi"]

print(rem(li,"ak"))

