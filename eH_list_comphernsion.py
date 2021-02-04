list1 = [2,3,4,5,6,7,8,9,10,1,44,24,342,343,243,21,4]
# list2 =[]
# for item in list1:
#     if item%2==0:
#         list2.append(item)

# print(list2)
#this above all can be done in 1 line -->shortcut to write the above alll in simple line

list2 = [i for i in list1 if i%2==0]

print(list2)

