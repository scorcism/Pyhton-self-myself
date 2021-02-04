# add a static method to problem no.2

class Calculator:
    def __init__(self,num):
        self.number = num

    def Square(self):
        print(f"the square of the number {self.number} is {self.number **2}")

    def SquareRoot(self):
        print(f"the squareroot of the number {self.number} is {self.number **3}")

    def Cube(self):
        print(f"the cube of the number {self.number} is {self.number **0.5}")

    @staticmethod
    def greet():
        print("*********************************hello***********************************")


a = Calculator(3)
a.greet()
a.Square()
a.SquareRoot()
a.Cube()
