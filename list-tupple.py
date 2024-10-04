# string

name = "hataf"

# name[0] = "g" #! string are immutable and therefore could not change
print(name)

# You can store any data type in a list and list is mutable and indexing is there 

random = ["hataf" , 2 , "zain" , True, None]
print(random)

random[0]= "ali" #! list are mutable and thus change

print(random)


# List Methods 

# Append Method 
newRandom = ["GK" , 24 , 25.5 , True , False]
random.append(newRandom)
print(random)

#clear list
# random.clear()
# print(random)

xrandom = random.copy()
print(f"Before change {xrandom}")
xrandom[0] = "xRandom"
print(f"After change {xrandom}")

#! tupple
#tuples are immutable , can carry any data type
tup = (2,2,3,3,"hataf", False,True) 

print(tup)








