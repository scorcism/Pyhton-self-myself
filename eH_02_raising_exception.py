def Increment(num):
    try:
        return int(num)+1

    except:
        raise ValueError("this is nor good")

a= Increment(3)

print(a)