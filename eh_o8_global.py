a =54#global variable
def func1():
    global a#mai yeh likh kar yeh bolta huu ki tum global wla ki value ko use karo
    print(f"thiss is when we put global a {a}")
    a=8 #local variable
    print(f"this is of local wla {a}")

func1()
print(f"this is of funcq ke neche wla {a}")