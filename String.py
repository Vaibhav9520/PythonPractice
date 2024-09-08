'''first_name="Rohit "
last_name="sharma"
print(first_name + last_name)

# we only add string with string ,If we add string with number then we found Error 
print(first_name + str(5)) # we change number into string by using str function

# String Slicing
str = "Pythonandjava"
print(str[1])
print(str[5])
print(str[2])
print(str[3])
print(str[-2])
print(str[-1::-1])
print(str[1::2])

# Q = Ask user name and print back user name in reverse order.
# [Hint: try to make your program in 2 lines using string formating]

username = "Iamrohitsharma"
print(username[-1::-1])

# String Methods
name = "VaIBHav Singh"
# 1 = len() function
print(len(name))
# 2 = lower() method
print(name.lower())
# 3 = upper() method
print(name.upper())
# 4 = title() method
print(name.title())
# 5 = count() method
print(name.count("a"))

# take two comma sapreted inputs from user
#  1.) user's name 
#  2.) a single charecter
 
#  Output:
#  1.) user's name lemgth
#  2.) count the charecter that user entered

user_name,user_charecter = input("Enter user_name and user_charecters:").split(",")
print(len(user_name))
print(user_name.count(user_charecter))
'''


# Replace() method  and find() method and center() mehod

string = "shr is a beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.find("beautiful"))
name = input("Enter your name:")
print(name.center(len(name)+8,"_"))