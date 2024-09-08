#Fucntions
'''
def add_two(a,b):
    c = a+b
    return c
a = int(input("a: "))
b = int(input("b: "))
print(add_two(a,b))
'''

'''
def add_name(a,b):
    c = a + b
    return c
a,b = input("Enter first and last name: ").split(",")
print(add_name(a,b))
'''

'''
def last_char(name):
    for i in name:
        print(i)
name = input("Enter your name: ")
print(last_char(name))
'''

'''
def odd_even(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter number: "))
print(odd_even(num))
'''

'''
def greater_two(a,b):
    if a >b:
        return a
    return b

a = int(input("Enter first numbers: "))
b = int(input("Enter second numbers: "))
print(greater_two(a,b))
'''
# default parameter
'''
def user_info(first_name,last_name,age = None):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
user_info("Vaibhav","Singh")
'''
# Scope 
'''
x = 55 #[Global veriable: Those veriable which define outside the function is called global veri0able.]
def func():
    x = 89 #[Local veriable : Those veriable which define inside the function is called local veriable]
    return x
print(func())  # here x is local veriable
print(x)    # here x is global veriable
'''
# Fibonacci series
def fibonacci_seq(num):
    a = 0
    b = 1
    if num == 1:
        print(a)
    elif num == 2:
        print(a, b)
    else:
        print(a, b, end=" ")
        for i in range(num-2):
            c = a + b
            a = b
            b = c
            print(b, end=" ")
num = int(input("Enter fiboncci number : "))
fibonacci_seq(num)

