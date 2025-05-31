m=int(input("From where you wanna start :"))
n=int(input("Where to finish : "))
sum=0
i=m
while i<=n:
    sum+=i
    i+=1
print("Summation : ",sum)

'''
alternative

#summation of series using range function
m=int(input("From where you wanna start :"))
n=int(input("Where to finish : "))
sum=0
for i in range(m,n+1,1):
    sum+=i
print("Summation : ",sum)
'''