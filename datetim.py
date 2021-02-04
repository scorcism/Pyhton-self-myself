import datetime

x = datetime.datetime.now()

print(x.strftime("%f"))#mili second
print(x.strftime("%b"))#month in full
print(x.strftime("%m"))#month
print(x.strftime("%d"))#date
print(x)#print the date year moth day time in sec and in mili sec