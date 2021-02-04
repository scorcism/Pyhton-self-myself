class Employe: #class attribute-->
    work = "google"  #this is specific to each class this #

abhi = Employe() # this is object instance
#instance can also have attribute
jash = Employe()
print(abhi.work) 
print(jash.work) 
Employe.work = "youtube" #this will change class work to youtube to acces this we will take employee ha s an argument
print(abhi.work) 
print(jash.work) 


# this will throw an error has the CLASS object has no attribute ADDRESS
# print(abhi.address)