class Employee():
    company = "google"

    def __init__(self,name,salary,workfor):#this will be print without providing any outpou to print
        self.name=name
        self.salary = salary
        self.workfor = workfor
        # print("this is in __init__")
        print(f"name is {self.name} salary is {self.salary} and works for {self.workfor}")


    def getSalary(self,signature):
        print(f"salary os the empolyee in {self.company} is  {self.salary} \n {signature}")

    @staticmethod
    def greet():
        print("good morining!")

harry = Employee("abhishek",500,"python")
harry = Employee() #-->this will throw an error
# harry.salary = 10000
# harry.getSalary("man") #Employee.getSalary(harry)
harry.greet()