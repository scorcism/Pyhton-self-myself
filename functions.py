def home(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100

marks1=[45,56,56,35]
percentage = home(marks1)

marks2 =[43,5,65,78]
percentage2 = home(marks2)

print(percentage,percentage2)