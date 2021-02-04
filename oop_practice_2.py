# write a class calculator capable of finding aquare cube and squareroot of a number

class Calculator:
    def __init__(self,num):
        self.number = num

    def Square(self):
        print(f"the square of the number {self.number} is {self.number **2}")

    def SquareRoot(self):
        print(f"the squareroot of the number {self.number} is {self.number **3}")

    def Cube(self):
        print(f"the cube of the number {self.number} is {self.number **0.5}")

a = Calculator(3)
a.Square()
a.SquareRoot()
a.Cube()

