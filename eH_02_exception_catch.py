try:
    a= int(input("enter your number : "))
    c =1/a
    print(c)

except ValueError as e:
    print("wriet num value only")

except ZeroDivisionError as e:
    print("avoid using 0")
    

print("thanks for playing")