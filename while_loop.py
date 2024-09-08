# While Statement
'''
a = 1
while a <=10:
    print("Hello while")
    a +=1
'''
# Q = Sum of n natural number and this number ask from the user and print the total from 1 to n
'''
n = int(input("Enter a number:"))
a = 1
total = 0
while a <=n:
    total += a
    a +=1
print(total)
'''
# Q = Ask user to input containing more than onr digit examlpe - 1256 and calculate the sum like 1+2+5+6 and print them.
'''
n = input("Enter more than one digitn number:")
sum = 0
a = 0
while a < len(n):
    sum += int(n[0])
    a +=1
print(sum)
'''
a = input("Plese enter your name:")
count=0
temp=""
while count < len(a):
    if a[count] not in temp:
        temp +=a[count]
        print(f"{a[count]} : {a.count(a[count])}")
    count +=1