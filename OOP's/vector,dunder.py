class vector:
    def __init__(self, i, j, k) -> None:
        self.i = i
        self.j = j 
        self.k = k 

    def __add__(self, x):
        return vector(self.i+x.i, self.j+x.j, self.k+x.k)

    def __str__(self):
        return (f"{self.i}i + {self.j}j + {self.k}k")

a = vector(9,2,3)
b = vector(3,5,8)
print(a)
print(b)
c = a+b
print(c)
print(type(c))