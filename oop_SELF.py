# when we remove self this will give an error
# self is a parimeter which automaticly passes

class Employee():
    company = "google"
    def getSalary(self):
        print(f"salary os the empolyee in {self.company} is  {self.salary}")

harry = Employee()
harry.salary = 10000
harry.getSalary() #Employee.getSalary(harry)
