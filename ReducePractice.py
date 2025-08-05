from functools import reduce
def add(x,y):
    return x+y
n=int(input("How many numbers you want to add on your list : "))
l=[]
for i in range(n):
    a=int(input(f"Enter number {i+1}: "))
    l.append(a)
print("Your list : ",l)
sum=int(reduce(add,l))
print("Summation of all numbers of your list : ",sum)