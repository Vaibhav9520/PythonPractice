string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
count1 = 0
count2 = 0
for i in string1:
    count1 +=1
for i in string2:
    count2 +=1
if count1 > count2:
    print("String First is larger in size")
elif count2 > count1:
    print("String Second is larger in size ")
else:
    print("Both strings are equal in length")
