
#! To Read file
# file = open("read-file.txt")
# read = file.read()
# print(read)
# file.close()

#! To Write file 
# fileRead = open("write-file.txt","w")
# write = fileRead.write("This is written by hataf")
# fileRead.close()

#! More functions 

# To read lines as a list from a file
# f = open("read-file.txt")
# lines = f.readlines()
# print(lines)
# f.close()

# print(f.readline()) #! Move to next line in a file every time it is called
# print(f.readline()) # !Move to next line in a file every time it is called
# print(f.readline()) # !Move to next line in a file every time it is called
# print(f.readline()) # !Move to next line in a file every time it is called
# print(f.readline()) # !Move to next line in a file every time it is called

#! Open each line using loop

# f = open("read-file.txt")

# i = 0
# while i <= 11:
#     print(f.readline())
#     i += 1

#! with statement => using with we can open and close file automatically 

with open("read-file.txt") as f:
    print(f.read())

