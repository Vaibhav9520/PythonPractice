# For loop
# for i in range(1,25):
    # print(f"Happy new year : {i}")

# Q = Sum of 1 to 10 numbers by using for loop
'''
num = int(input("Enter a number:"))
total = 0
for i in range(1,num+1):
    total +=i
print(f"sum : {total}")
'''
# Q = 2
'''
total = 0
num = input("Enter a number:")
for i in range(0,len(num)):
    total +=int(num[i])
print(f"sum : {total}")
'''
# Q = 3
'''
name = input("Enter your name: ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]
'''
# For loop with string
name = "Vaibhav singh"
for i in name:
    print(i)