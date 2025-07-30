import numpy as np

nums=[]
a=int(input("How many students marks you want to add : "))
for i in range(a):
    x=int(input(f"Enter mark of student no {i+1} : "))
    nums.append(x)
arr=np.array(nums) 
print("Maximum number amongst them : ",np.max(arr))
print("Minimum mark : ",np.min(arr))
print("Average mark : ",np.mean(arr))
print("Total mark : ",np.sum(arr))

