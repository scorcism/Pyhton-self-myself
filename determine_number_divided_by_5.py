l = [1,2,3,4,5,6,7,8,9,10]

a = filter(lambda a: a % 5 == 0, l)#here we have lambda function

print(list(a))
