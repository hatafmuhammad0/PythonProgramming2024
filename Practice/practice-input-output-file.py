
#! Write a table in different files
# def genrateTable(n):
#     table = ""

#     for i in range (1,11):
#         table += f"{n} x {i} = {n*i} \n"
#     with open(f"table/table_{n}.txt","w") as f:
#         f.write(table)



# for i in range(2,21):
    
#     genrateTable(i) 

#! a file contain word "donkey" many times you need to replace it with "cow"

# def replaceWord(oldword,newWord,fileName):
#     with open(fileName) as f:
#         content = f.read()
#         with open (fileName,"w") as w:
#             w.write(content.replace(oldword,newWord))

# replaceWord("cow","lion","test1.txt")

#! Write a program for a list of such words to be censored

# li = ["click me" , "buy now" , "click here"]

# def replaceWord(list,fileName):
#     for i in list:
#         with open(fileName) as f:
#             content = f.read()
#             with open (fileName,"w") as w:
#                 w.write(content.replace(i,"####"))

# replaceWord(li,"test1.txt")

#! Mine a log file to find out whether it contain "python" in it or not?

# with open("log.txt") as f:
#     content = f.read()
#     print(f'{"python" in content}')

#! Write a program to find out line number in which "python" is present?

# with open("log.txt") as f:
#     ls = f.readlines()
#     lineNum = 0
#     for i in ls:
#         lineNum +=1
#         if "python" in i:
#             print(f"Python is presnet in line number : {lineNum} and content of line is : {i}")
#             break

#! Write a program to make a copy of a " this.txt" to "file.txt"
 
# with open("this.txt") as t:
#     content = t.read()
#     with open("this-copy.txt","w") as f:
#         f.write(content)

#! Write a program to find out whether the content of 1 file matches with another file?

# with open("this.txt") as t:
#     thisContent = t.read()
    
# with open("this-copy.txt") as tc:
#     thisCopyContent = tc.read()
        
# if thisCopyContent == thisContent:
#     print("Both content matches ")
# else:
#     print("No match found")

#! Wipe out the content of a file

# with open("wipe.txt","w") as w:
#     w.flush()

#! Write a python program to rename a file to "rename_by_python"


