class Employee():
    company = "google"

    def __init__(self):#this will be printed automaticly withour any argument
        print("this is in __init__")


    def getSalary(self,signature):
        print(f"salary os the empolyee in {self.company} is  {self.salary} \n {signature}")

    @staticmethod
    def greet():
        print("good morining!")

harry = Employee()
harry.salary = 10000
harry.getSalary("man") #Employee.getSalary(harry)
harry.greet()