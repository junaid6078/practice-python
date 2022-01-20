import numpy as np
import pandas as pd
import math
array1=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
#print([[math.sqrt(i) for i in row ] for row in array1])

array2=np.array([[1,2,3],
                 [4,5,6]])
#print([[math.sqrt(i) for i in row ] for row in array2])
#print(np.sqrt(array2))
#print(array1.sum(axis=0))
#print(array1.sum(axis=1))
#print(array1[1,:2])
#print(np.arange(10).reshape(2,5))
#print(np.random.rand(2,3))

##########view vs copy
subset=array2[: , :2].copy()
#print(subset)
subset[0,0]=1000
#print(subset)
print(array2)
