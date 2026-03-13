#finding logarithms using math module and numpy arrays

import math
import numpy as np

#finding natural logarithms

print(math.log(1288))
print(math.log(2.73))
print(math.log(0.00000000000000001))
print(math.log(1))

#finding base 10 logarithms

print(math.log10(10))
print(math.log10(1))
print(math.log10(394))

#finding base 2 logarithms

print(math.log2(2))
print(math.log2(256))

#finding natural log for a numpy array

my_array = np.array([1,2,3,100,2.7128,1929,34])
np.log(my_array)
