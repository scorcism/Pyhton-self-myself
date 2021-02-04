class Number:
    def __init__(self,num):
        self.num =num

    def __add__(self,num2):#this is operator overloading 
        print("lets add..")
        return self.num + num2.num #if we write here 1000 then thousand will be printed

    def __mul__(self,num2):
        print("lets mul..")
        return self.num * num2.num 

    def __str__(self):#this is use when you want to directly ptiny the object
        return f"the decimal : {self.num}"

n =Number(9)
print(n)#to print this number we will use STR method


print(len(n))

