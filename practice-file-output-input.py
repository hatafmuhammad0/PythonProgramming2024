
#! Write a program to read text from a file and check if it contain a word in it if yes then return that line? 

def finder(li,word):
    for i in li:
        if word in i:
            print(i)


with open("poem.txt") as li:
    x = li.readlines()
    

finder(x,"good")