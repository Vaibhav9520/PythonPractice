# Two inputs in a single line
name , age = "Rohit", 25
print(name)
print(age)

# If we want to take two inputs from the user in a single line
# name , age = input("Enter your name and age: ").split(",")
# print(name)
# print(age)

#String Formating
name = "Rohit"
age = 25
# by help of python 3
print("Your name is {} and your age is {}".format(name,age))

# by help of python 3.6
print(f"Your name is {name} and your age is {age}")

#Q= Ask user to input 3 numbers and you have to print avrage of three numbers using string formating [Hint: all three comma seprated inputs in one line.]
num1,num2,num3 = input("Enter num1,num2 and num3:").split(",")
average = (int(num1)+ int(num2) + int(num3))/3
print(f"The average of num1,num2a and num3 is {average}")