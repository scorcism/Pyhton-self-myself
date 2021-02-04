#here we are going to know about how we can create a function to specify that th einput age is greater then or less then
# 18

a =int(input("Enter your age: "))
if a==18:
    print("your age is equal to 18")

elif a>18:
    print("your age is greater then 18")

# elif a<18: #here we can omit the a<18 part has there is no option left in the function
#     print("your age is less then 18! Drink complan")

else:
    print("your age is less then 18! Drink complain")