class Employe: 
    work = "google" 

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