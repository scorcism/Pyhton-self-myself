
print("Welcome to the game ")

name = input("enter your name: ")
age =int(input("Enter your age: "))

print("Hello",name,"you are",age,"years old")

if age>=18:

    print("Congratulations! You are eligible to play this game\n")
    a =  input('''Choose between health / welth :  ''').lower()
    if a == "health":
        print("You have choosen the right path!! Lets play!! ")
        choice_between = input('''what is more precious? DIAMON / TREE: ''').lower()

        if choice_between =="tree":
            print("Yes you are right. TREES are more precious ")
            another_level =input("Lets go to another level. Choose between (1:advantages/2:disadvanatges)")

            if another_level == "advantages":
                print("It provide us air so we can survive. for more info go to GOOGLE")
            else:
                print("There are no disadavntages")
        else:
            print("You are fool")
    else :
        print("Opps! you hav choosen the wrong path!!")

else:
    print("Your age is less then the credentials !! you can rest now! RIP")

print("Thanks for playing the game...")

