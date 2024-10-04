#Display a user entered name followed by good morning 
# userName = input("Enter user Name : ")
# print(f'Good Morning! {userName}')

# Write a program to fill letter template 
# from datetime import datetime



# print(f'''
#       Dear {userName};
#       You are Selected!
#       {datetime.now().date()}''')

letter = '''
Dear |<Name>|
You are Selected
|<Date>|'''

letter = letter.replace("|<Name>|", "ARK")
letter = letter.replace("|<Date>|" , "October 10, 2024")

print(letter)

# Write a program to detect double spaces in a string 

spacechecker = "Muhammad  Hataf"

print(spacechecker.count("  "))

# Replace the double space in above question with single space

print(spacechecker.replace("  "," "))



