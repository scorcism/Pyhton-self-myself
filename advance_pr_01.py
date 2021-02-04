def Readfile(filename):
    try:  
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"try the file which wxists error {filename}")

Readfile("1.txt")
Readfile("2.txt")
Readfile("3.txt")