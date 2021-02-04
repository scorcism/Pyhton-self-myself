# write a class train which has methods to book  a ticket ,get status (no of seats) and 
# get fare information of trains running under indain railways


class Train:
    def __init__(self,name,rate,seat):
        self.name = name
        self.rate = rate
        self.seat = seat

    def getstatus(self):
        print("###################2")
        print(f"the name of the train is {self.name}")
        print(f"the rate is rs. {self.rate}")
        print("&&&&&&&&&&&&&&&&7")

    def getrateinfo(self):
        print(f"the rate  in the train are {self.rate}")

    def getbookticket(self):
        if (self.seat > 0):
            print(f"your ticket is being bookes! your ticket number is {self.seat}")
            self.seat = self.seat - 1
        else:
            print("no more seats available go for tatkal")






atrain = Train("rajdhani express",90,30)
atrain.getstatus()

atrain.getrateinfo()

atrain.getbookticket()
atrain.getbookticket()














