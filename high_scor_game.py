#if the score is greater then highscore.txt then this function will overide the highscore
# and if the function is less then it will not perfprm any trask

def game():
    return 64

score=game()
with open("highscore.txt") as f:
    highscore =int(f.read())

if highscore<score:
    with open("highscore.txt","w") as f:
        f.write(str(score))

