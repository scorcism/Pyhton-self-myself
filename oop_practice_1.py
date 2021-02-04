# create a class programmer for storing information of few programmers working at microsoft

class Programmer:
    company ="microscoft"

    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getInfo(self):
        print(f"the name of the {self.company} programmer is {self.name} and the wd is {self.product}")

jash =Programmer("jash","word")
yash = Programmer("yash","powerpoint")

jash.getInfo()
yash.getInfo()

