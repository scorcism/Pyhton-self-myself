class Number:
    def __init__(self,num):
        self.num =num

    def __add__(self,num2):#this is operator overloading 
        print("lets add..")
        return self.num + num2.num #if we write here 1000 then thousand will be printed

    def __mul__(self,num2):
        print("lets mul..")
        return self.num * num2.num 
        
n1 = Number(6)
n2 = Number(5)
sum = n1 + n2
print(sum)

n1 = Number(6)
n2 = Number(5)
mul = n1 * n2
print(mul)







