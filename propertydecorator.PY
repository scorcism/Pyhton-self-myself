class Employee:
    company = "bharat gass"
    salary =5600
    salaryBonus = 400

    @property #(GETTER)this is a function which command all the function inside this so it will bw performed internally anf the single output will be given out
    def totalsalary(self):
        return self.salary + self.salaryBonus
    
    @totalsalary.setter #to set the values
    def totalsalary(self,val):
        self.salaryBonus = val - self.salary


e = Employee()

e.salaryBonus
print(e.totalsalary)
e.totalsalary = 5800 #here er have initilised the total salary to constant so we will make a function which will automatially adjest the salary bonus for that we will use SETTER

print(e.salaryBonus)
print(e.salary)
print(e.totalsalary)