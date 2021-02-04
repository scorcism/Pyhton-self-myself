# create a class c2d vector and use it to create another class representing a 3d vector

class c2dvec:
    def __init__( self, i, j ):
        self.icap = i
        self.jcap = j

    def __init__(self,i ,j ):
        return f"{self.icap +self.i }+ {self.jcap + self.j}"

class c3dvec(c2dvec):
    def __init__(self , i , j , k ):
        super().__init__( i , j )
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    

me = c2dvec(1,3)

he = c3dvec(1,3,5)

print(v2d)
print(v3d)