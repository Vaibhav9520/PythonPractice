# n=int(input("Enter a number: "))
# val=1
# sum=0
# for i in range(1,n):
#     if(i<=n):
#         sum=sum+val
#         val = val+1
#     else:
#         break
# print(sum)
n = int(input("Enter any number: "))
fact = 1
for i in range(1,n+1):
    if(i<=n):
        fact= fact*i
print("Factorial",fact)
