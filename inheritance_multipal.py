class Employee:
    companey = "visa"
    rcode= 120

class freeleancer:
    comaney ="fiverr"
    level = 0

    def upgradelevel(self):
        self.level =self.level +1 


class programmer(Employee,freeleancer):
    name= "rohan"

p = programmer()
p.upgradelevel()
# p.upgradelevel()
# p.upgradelevel()
# p.upgradelevel()
print(p.level)