from operator import mul
from functools import reduce
import numpy as np

factorial = lambda x: reduce(mul, range(1, x+1))

print(factorial(6))

x = np.matrix('1;3;4')
print(x)