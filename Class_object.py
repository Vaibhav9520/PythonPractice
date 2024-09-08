class students:
    def printdetails(self):
        print("Your name is :",self.name)
        print("Your rollno is :",self.rollno)
rahul = students()
rahul.name="Rahul"
rahul.rollno = "12208986"
rahul.printdetails()

amrita = students()
amrita.name="Amrita"
amrita.rollno = "12563986"
amrita.printdetails()


class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Sum is :",a+b)
obj=calculator(5,8)
