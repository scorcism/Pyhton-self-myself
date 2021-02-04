
print("Lets play the holy shit\n")

import random
randNumber = random.randint( 1, 100)
# print(randNumber)
guessednu = None
guesses= 0

while (guessednu != randNumber):
    guessednu = int(input("Enter th guessed number:"))
    guesses += 1
    if (guessednu == randNumber):
        print("Congratulation!! Your number is correct")
    else:
        if (guessednu > randNumber):
            print("Your number is wrong !! PLease select low value number")
        else:
            print("Your number is wrong !! PLease select higher value number")

print(f"you guesses the number in {guesses} guesses")

with open("numberGUESShighscor.txt","r") as f:
    highscor=int(f.read())

if guesses<highscor :
    print("you have broken the records")
    with open("numberGUESShighscor.txt","w") as f:
        f.write(str(guesses))




