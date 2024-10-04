#! Dictionary => is a collection of key value pairs.

#Properties: 
# 1) It is unordered 
# 2) It is mutable 
# 3) It is indexed 
# 4) Can not contain duplicate Keys 

# example 1: 

user = {
    "name" : "Hataf",
    "userId" : "1",
    "marks" : 78,
    "list" : [2,3,4],
}

user["name"] = "Ali"

print(user)

# user.pop("marks")
# print(user)
user.update({"password":"zksyncera"}) #! this will update value and if key value not there it will add it in a dictionary
print(user)

#! What is the difference between below two things? 
print(user.get("name")) # output : Ali 
print(user["name"]) # output : Ali
#print(user.get("name1")) #! output :As Name1 is not a key thus output is  returns "None"
#print(user["name1"]) #! output : As Name1 is not a key thus output is  returns "Error" 

# ! ===============>>>>>>>>  Set <<<<<<<<<<<<===============
'''
# Properties :
1) Sets are unordered : Elements order doesn't matter 
2) Sets are unindexed : Can not access elements by index 
3) There is no way to change items in sets 
4) Sets do not contain duplicate values 
'''

# Operations on Sets 

set1 = {1,"apple" , True}
print(set1)

set2 = {2,3,"orange","grapes",False}
print(set2)

#! Using set we can also perform Methametical operations
# Union , Intersection , difference
# how to write empty dictionary and sets? 

dic1 = {} #empty dictionary
set3 = set() #empty set
print(type(dic1))
print(type(set3))

#! Set Methods

set4 = {2,"hataf","A","a","A",24,24,24}
print(set4)

print(len(set4)) #Length of a set
set4.remove(24) #Remove item from a set
print(set4)

set5 = {2,"hataf","A","a","A",24,24,24}











































































