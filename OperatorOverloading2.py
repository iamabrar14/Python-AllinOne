class calculation:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return f"{self.a} and {self.b}"
    def __mul__(self,x):
        return self.a*x.a,self.b*x.b

c1=calculation(10,3)
print(c1)
c2=calculation(4,5)
print(c2)
print(c1*c2)
""" here 10*4 and 3*5 happened
"""