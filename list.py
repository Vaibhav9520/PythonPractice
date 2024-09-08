# list
'''
list1 = ['one','two','three',1,2,3,8.5]
print(list1)
print(type(list1))
'''
# append
'''
fruits = ['grapes','apple']
print(fruits)
fruits.append("mango")
print(fruits)
'''
# Insert
'''
fruits=['hello','hii','hey']
fruits.insert(2,"bye")
print(fruits)
'''
'''
list1=['one','two','three']
list2=['1','2','3']
list1.extend(list2)
print(list1)
list2.append(list1)
print(list2)
'''
#  deliting method
'''
list1=['one','two','three','four']
list1.pop()#if we not pass argument with pop then it delet last element from list
print(list1)
list1.remove('one')
'''
#for add data in list we use {append},{insert},{extend}
#for remove data in list we use {pop},{del},{remove}
#count
# fruits=['apple','apple','orange','grapes','mango','banana']
#print(fruits.count('apple'))
# print(fruits.sort())
# print(sorted(fruits))
# print(fruits.clear())'''
#  for compare the lists we can use {== or is}

# def list1(l):
#     square2 = []
#     for i in l:
#         square2.append(i**2)
#     return square2
# num = list(range(1,11))
# print(list1(num))
'''
def reverse_list(l):
    new_list = []
    for i in range(len(l)):
        pooped_list = l.pop()
        new_list.append(pooped_list)
    return new_list
num = list(range(1,11))
print(reverse_list(num))
'''
# def reserved_list(l):
#     new_list = []
#     for j in l:
#         new_list.append(j[::-1])
#     return new_list
# num = ['abc','tuv','xyz']
# print(reserved_list(num))
'''
def odd_even(l):
    even_num = []
    odd_num = []
    for i in l:
        if i%2==0:
            even_num.append(i)
        else:
            odd_num.append(i)
    output = [even_num,odd_num]
    return output
num = list(range(1,11))
print(odd_even(num))
'''
def filter_list(l,m):
    new_list = []
    for i in l and m:
        new_list.append(i)
    return new_list
l = [1,2,3,4,5,6]
m = [2,5,4,9,8]
print(filter_list(l,m))