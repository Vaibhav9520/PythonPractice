a =input("Enter String: ")
count1 = 0
count2 = 0
for i in a:
    if (i.islower()):
        count1 +=1
    elif (i.isupper()):
        count2 +=1
print("Lower letters in given string is :",count1)
print("Upper letters in given string is :",count2)
