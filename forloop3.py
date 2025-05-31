#range function
m=int(input("From where you wanna start :"))
n=int(input("Where to finish : "))

print("Your numbers are : ")
for i in range(m,n+1,1): #n+1 cause iteration will stop 1 less than n so we added 1
    print(i)
