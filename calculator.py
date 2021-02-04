#lets make a simple calculator

print("welcome to the calculator")
while True:

    print("Enter the number for operation or q to quit\n")
    first_input = input('''chosse between the following operations
    [+] to add
    [-] to subtract
    [*] to multiply
    [/] to devide
     option: ''')
    if first_input != "q":
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))


        if first_input == "+" :
              print(f"the sum of {num1} and {num2} is {num1 + num2}\n")

        elif first_input == "-" :
            print(f"the substraction of {num1} and {num2} is {num1-num2}\n")

        elif first_input == "*" :
            print(f"the multiplication of {num1} and {num2} is {num1*num2}\n")

        elif first_input == "/" :
            print(f"the division of {num1} and {num2} is {num1/num2}\n")
    else:
        print("Thanks for using the calculator! ")
        break


#you make more elobratable calculator
# thank for watching
# scor32k


