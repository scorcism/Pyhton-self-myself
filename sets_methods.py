a =set()
print(a)

a.add(5)#add the value in the set
a.add(7)
a.add(8)
print(a)

print(len(a))#gives the length

a.remove(6)#will rwmove 5 from the list
print(a)

a.remove(15)#throws an as there is no 15
print(a)

#adding the value repitedly does not change the set

a.add([5,3,5])#we cannot add list and dictioney in the set has they can be changed
print(a)


a.pop()#this will removw any 