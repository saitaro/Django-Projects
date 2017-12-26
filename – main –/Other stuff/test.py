from operator import mul
from functools import reduce

factorial = lambda x: reduce(mul, range(1, x+1))

print(factorial(6))