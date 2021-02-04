class Employee:
    companey = "harved"
    salary = 100
    location = "mumbra"

    # def changeSalary(self):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal

e= Employee()
print(e.salary)
e.changeSalary(400)
print(e.salary)

    
