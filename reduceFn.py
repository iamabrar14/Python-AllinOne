from functools import reduce
def mySum(x,y):
    return x+y
l=[1,2,3,4,5]
sum=reduce(mySum,l)
print("Sum of whole list : ",sum)