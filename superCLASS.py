# super can also be user to call a constructor

class person:
    country ="India"
    def takebreadth(self):
        print("i m breathimg from person")

class employee(person):
    company ="honda"
    
    def getsalary(self):
        print(f" im an employee and i am earning this much")

    def takebreadth(self):
        print("i m to be an human  from employee")

class programmer(employee):
    company = "fiverr"

    def getsalary(self):
        print(f" im programmer so no earnings")

    def takebreadth(self):
        super().takebreadth()# super means yeh hai ki programmer class ka jo sper hai means jisse yeh derive hua hai usko bhi ye use karega
        print("i m breathimg++ from programmer")


p =person()
p.takebreadth()
e = employee()
e.takebreadth()
pr = programmer()
pr. takebreadth()
