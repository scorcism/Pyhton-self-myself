def  Square(num):
    return num*num

# method 1
l =[1,2,3]
l2 =[]
for itrm in l:
    l2.append(Square(itrm))
print(l2)

# method 2
# using MAP
print(list(map(Square,l)))