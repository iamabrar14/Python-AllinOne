def func(f):
    if f%2==0:
        return f
    

a=int(input("How many numbers :"))
p=[]

for i in range(a):
    b=int(input(f"Enter number{i+1}:"))
    p.append(b)
    
newl=list(filter(func,p))
print("Even Numbers : ",newl)