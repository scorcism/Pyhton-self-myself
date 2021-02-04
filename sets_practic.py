mydict ={
    "saamans":"item",
    "insaan":"human",
    "faltu":"kachra"
}
print("the hindi words are",mydict.keys())
a =input("enter the hindi word :\n ")
#to aviod error we will use get
print("the meaning of the word is : ", mydict.get(a)) 