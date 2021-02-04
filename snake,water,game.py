import  random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp=="s":
        if you=="g":
            return True
        elif you=="w":
            return False
    elif comp=="g":
        if you=="s":
            return True
        elif you=="w":
            return False
    elif comp=="w":
        if you=="s":
            return True
        elif you=="g":
            return False

comp= print("i have selected its your turn  ")#1st start your project from here  then analise
randno= random.randint(1,3)
if randno==1:
    comp ="s"
elif randno==2:
    comp = "g"
elif randno==3:
    comp= "w"

you=input("Select from : Snake(s) Gun(g) or Water(w)")

a=gamewin(comp,you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a==None:
    print("the game is tie!")
elif a:
    print("you win!")

else:
    print("you loose!")
