import numpy as np

nums=[]
a=int(input("How many numbers you want to add : "))
for i in range(a):
    x=int(input(f"Enter number {i+1} : "))
    nums.append(x)
print("New list : ",nums)
arr=np.array(nums) #Converting list into array
print("List to Array : ",arr)