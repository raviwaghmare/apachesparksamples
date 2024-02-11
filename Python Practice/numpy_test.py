from __future__ import division
import numpy as np

arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr1[0][1])
print(arr1/2)

arr2 = np.arange(0,11)
print(arr2)

arr_zero = np.zeros((10,10))
print(arr_zero)
arr_length=arr_zero.shape[1]
print(arr_length)

for i in range(arr_length):
    arr_zero[i]=i
    
print(arr_zero)

arr1 = np.arange(50) #.reshape((10,5))
print(arr1)