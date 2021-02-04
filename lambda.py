# def func(a):
#     return a+5

# x =563
# print(func(x))

# performing this using lambda function
# func lambda parameter_list: expression
func =  lambda a: a+5
square = lambda x: x*x
sum = lambda a, b, c: a+b+c
x =4
print(func(x))
print(func(square(x)))
print(sum(x,1,4))
