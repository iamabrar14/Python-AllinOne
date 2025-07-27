"""NumPy (Numerical Python) is a powerful Python library used for numerical computations. 
It provides support for multidimensional arrays, 
mathematical functions, linear algebra, Fourier transforms, and more.
"""
import numpy as np
a=np.array([1,2,3,4,5,6]) #1D array
b=np.array([[1,2,3],[4,5,6]]) #2D array
print("A : ",a)
print("B : ",b)
#reshape a
reshaped=b.reshape((3,2))
print("Reshaped b : ",reshaped)