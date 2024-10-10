
#! Age group categorization
#~Classify a age group : Child (1 < 13) , Teenager (13-19) , Adult(20-59) , Senior(60+)

# def ageGroupClassification(age):
#     if age >= 1 and age <=13:
#         print(f"Your age is {age} and you are classify as child") 
#     elif age >13 and age <=19:
#         print(f"Your age is {age} and you are classify as Teenger") 
#     elif age >=20 and age <=59:
#         print(f"Your age is {age} and you are classify as Adult") 
#     elif age >= 60:
#         print(f"Your age is {age} and you are classify as Senior") 
#     else:
#         print("Type correct age")

# age = int(input("Type you Age : "))
# ageGroupClassification(age)

#! Movie ticket pricing : 
#~ Price are based on age , $12 for Adults (age> 18) and $8 for childrens and 2% discount if day is "Wednesday"

# age = int(input("Enter your age : "))
# day = input("Enter day : ").lower()

# if age <= 18 and day == "wednesday":
#     print(f"Ticket price for Children is Orignal price $8 \n Wednesday Discount -{8*0.02} \n After dicount price is {8 - (8*0.02)}")
# elif age > 18 and day == "wednesday":
#     print(f"Ticket price for Adult is Orignal price $12 \n Wednesday Discount -{12*0.02} \n After dicount price is {12 - (12*0.02)}")
# elif age <= 18 :
#     print(f"Ticket price for Children is Orignal price $8")
# else:
#     print(f"Ticket price for Adult is Orignal price $12")

#! Fruit ripiness checker 
#~ Green -Unripe , Yellow - ripe , Brown - over ripe)

# fruitColor = input("Write Fruit color : ").lower()

# def ripinessChecker(color):
#     if color == "green":
#         print("Unripe")
#     elif color=="yellow":
#         print("ripe")
#     else:
#         print("over ripe")

# ripinessChecker(fruitColor)

#! Password checker 
#~ Weak < 6 char , Medium (6-10) charc , Strong > 10

# ChekPassword = input("Enter your password : ")

# if len(ChekPassword) <6:
#     print("Weak password")
# elif len(ChekPassword) >=6 and len(ChekPassword) <= 10:
#     print("Medium password")
# else:
#     print("Strong password")





        
