#lets make a program whuch will calculate a factorial of a given number

def FactorialNumber(fac):
    if fac ==0 or fac == 1:
        return 1
    else:
        return fac * FactorialNumber(fac-1)

# :)
if __name__ == '__main__':
    fac= int(input("Enter the number: "))
    number= FactorialNumber(fac)
    print(f"the factorial of the number is {number}")