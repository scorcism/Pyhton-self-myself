def  Greater_then_5(num):
    if num>5:
        return True
    else:
        return False
        
g10 = lambda num: num>10
l = [1,2,3,4,5,6,7,8,9,5,56,5,64,3,65,63,44]
print(list(filter(Greater_then_5,l)))
print(list(filter(g10,l)))