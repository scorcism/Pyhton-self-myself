#this is to find if the function is available or not
#connected to teinkelstar.txtn wla
f = open("twinkelSTAR.txt","r")

lit = f.read()
if "twinkel" in lit:
    print("twinkel is present")

else:
    print("twinkel is absent")

f.close()