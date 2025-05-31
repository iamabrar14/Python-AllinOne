#summation of series using range function
m=int(input("From where you wanna start :"))
n=int(input("Where to finish : "))
multi=1
for i in range(m,n+1,1):
    multi*=i
print("Multiplication : ",multi)