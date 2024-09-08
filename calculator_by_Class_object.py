# Making a calculator by using class Constructor
class calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mult(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

obj = calculator(a,b)
choice = 1
while choice!=0:
    print("Enter 0 for exiting")
    print("Enter 1 for adding")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplaction")
    print("Enter 4 for division")
    choice = int(input("Enter the value of choice: "))
    if choice == 1:
        print("Result is :",obj.add())
    elif choice == 2:
        print("Result is :",obj.sub())
    elif choice == 3:
        print("Result is :",obj.mult())
    elif choice == 4:
        print("Result is :",obj.div())
    elif choice == 0:
        print("Existing")
    else:
        print("Invalid Choice")








    

            
