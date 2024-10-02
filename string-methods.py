name = "hataf"
fullName = "!!!Muhammad Hataf!!!"
newcheck = "0123456789"

print(name.upper())
print(name.lower())
print(name.capitalize())
print(fullName)
print(fullName.rstrip("!")) #! output => !!!Muhammad Hataf
print(fullName.replace("Hataf","Harry"))
print(fullName.split(" "))
print(fullName.count("a"))
print(fullName.endswith("!"))
print(newcheck.endswith("4",0,5))
print(newcheck.find("41")) #! give -1 if no value found

# print(newcheck.index("41")) #!find the index of given value and if not found give value Error 
