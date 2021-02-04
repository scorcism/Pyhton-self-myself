#in this if the object instance also has the same attriute SIMILAR to the class object then the funcion will go fro the OBJECT ATTRIBUTE


class Employe: 
    work = "google" 
    salary = 100

abhi = Employe() 
jash =Employe()
abhi.salary = 300
jash.salary = 400


print(abhi.work) 
print(jash.work)
Employe.work = "youtube" 
print(abhi.work)
print(jash.work)
print(abhi.salary)
print(jash.salary)

abhi = Employe() 
jash =Employe()
abhi.salary = 300
jash.salary = 400

print(abhi.work) 
print(jash.work)
Employe.work = "youtube" 
print(abhi.work)
print(jash.work)
print(abhi.salary)
print(jash.salary)