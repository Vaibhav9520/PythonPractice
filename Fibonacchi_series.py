#Fibbonacchi Series
num = int(input("Enter any number:"))
n1 , n2 = 0,1
sum = 0
if num <=0:
    print("Plese enter number greter than 0")
else:
    for i in range(0,num):
        print(sum,end=',')
        n1=n2
        n2 = sum
        sum  = n1+n2










# by reccurrion
def fibonacci(n):
    if n ==1 or n == 0:
        return n;
    else:
        return fibonacci(n-2) + fibonacci(n-1)
num = int(input("Enter a positive number :"))
if num < 0:
    print("Invalid Number")
i = 0
print("Fibonacci series: ")

for i in range(0,num):
    print(fibonacci(i))












































