import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9])

print(np1[1:5]) #2,3,4,5
#from 1 until 5 (not till 5)

print(np1[4:]) #4->end

print(np1[-3:-1]) #start from back

print(np1[1:5:2]) # , ,steps

print(np1[::2]) #skip one

np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np2[1,2]) #8