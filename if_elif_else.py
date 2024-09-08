# If Statement
'''
age = input("Enter your age :")
age = int(age)
if age >= 18:
    print("You are above 18")
'''
# Pass Statement
'''
x = 18
if x > 18 :
    pass # it is used to pass the loop and if we have noting to print then we wright it
'''
'''# Elif Statement
x = int(input("Enter Last date of month: "))
if x == 30:
    print("April,June,September,Novenber")
elif x == 31:
    print("Janbary,March,May,July,Augest,October,Decenber")
else:
    print("Ferbery")'''

# Q =  Make a veriable,like winning_number and assign any number to it.  
# Ask user gess a number
# If user gussed correctly number then print "YOU WIN!!!.
#if user did't gussed correctly number then:
# if user gussed lower than acctule number then print "TOO LOW!!!
# if user gussed higher than actul number then print "TOO HEIGH!!

'''
winning_number = 75
guss_number = int(input("Enter guss_number: "))
if guss_number == winning_number:
    print("YOU WIN THE GAME")
elif guss_number < winning_number:
    print("YOUR NUMBER IS TOO LOW")
elif guss_number > winning_number:
    print("YOU NUMBER IS TOO HEIGH")
else:
    print("YOU ENTEREN WRONG INPUT AND YOU TERMMINATED FROM THE GAME")'''

# Q =  WATCH COCO
#  Ask user's name and age
# if user name start with ('a' or 'A') and age is above 10 then print "you can watch coco movie"
# else print "sorry, you cannot watch coco"
user_name,user_age = input("Enter user's name and age:").split(",")
user_age = int(user_age)
if (user_name[0] == 'a' or user_name[0] == 'A') and user_age >= 10:
    print("You can watch coco movie")
else:
    print("Sorry, you can't watch movie")