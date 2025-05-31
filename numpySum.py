#sum of array elements
import numpy as np 
n=int(input("How many numbers do you want in array ?"))
my_array=np.arange(1,n+1)
print(my_array)
sum=np.sum(my_array)
print("Sum of these numbers are : ",sum)
