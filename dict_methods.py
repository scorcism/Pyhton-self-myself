fast ={
     "name":"abhishek",
     "age": [17] ,
     "food":["bananan","mangu"],
     "extra":{"name":"player"},
}
print(fast.keys())#normally print the dictonsry

print(type(fast.keys()))# print the type

print(list(fast.keys())) #this will print the keys in list format

print(fast.values()) #values

print(fast.items())#print all the conrtents in the dictionary

print(fast)

myupdate= {
    "surya":"friend"
}

fast.update(myupdate)#use to update the dictionaryc
print(fast)