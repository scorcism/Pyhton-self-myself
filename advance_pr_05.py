num = int(input("Enter the number : "))

table = [(num*i) for i in range(1, 11)]

print(table)

with open("tablesss.txt","a")as f:
    f.write(str(table))