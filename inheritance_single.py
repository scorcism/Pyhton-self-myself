# single inheritance

class Employee:
    companry = "google"

    def showDetails(self):
        print("this is the showdetails of employee")

    def printme(self):
        print("this is the prine me of employee")

class programmer(Employee):
    companry = "youtube"

    def printme(self):
        print("this is prinrme of programmer")


e =Employee()
p = programmer()


e.showDetails()
p.showDetails()#this is inherited from the father class 
print("############################")

e.printme()
p.printme()#this becz the child class incress code reusability
