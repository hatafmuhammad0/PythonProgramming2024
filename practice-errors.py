
#? Write a program to open 3 files , if any these files are not present , a message without exiting the program must br printed promoted the same 

# try:
#     with open("1.txt") as file1:
#         pass 
# except:
#     print("1.txt not exsist")

# try:
#     with open("2.txt") as file2:
#         pass 
# except:
#     print("2.txt not exsist")

# try:
#     with open("3.txt") as file3:
#         pass 
# except:
#     print("3.txt not exsist")

#? Write a program thrid ,fifth and seventh element from a list using enumerate function

# li = ["1st","2nd","3rd","4th","5th","6th" ,"7th"]

# for index,items in enumerate(li,1):
#     if index == 3 or index == 5 or index == 7:
#         print(f"index {index} and items : {items}")

#? Write a list comprehension to print a list which contains the multiplication of a user entered number 

# tableNumber = int(input("Enter table number : "))

# tableList = [tableNumber*i for i in range(1,11) ]

# for i in range (1,10):
#     tableList.append(f"{tableNumber} * {i} = {tableNumber*i}")

# print(tableList)

#? Store multiplication table in a text file


tableNumber = int(input("Enter table number : "))

for i in range (1,11):
    tableList = [tableNumber*i for i in range(1,11) ]
    with open("table.txt","w") as f:
        f.write(f"{tableNumber} * {i} = {str(tableList)}")
