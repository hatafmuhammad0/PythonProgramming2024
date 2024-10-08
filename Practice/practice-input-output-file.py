
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

def replaceWord(oldword,newWord,fileName):
    with open(fileName) as f:
        content = f.read()
        with open (fileName,"w") as w:
            w.write(content.replace(oldword,newWord))

replaceWord("cow","lion","test1.txt")