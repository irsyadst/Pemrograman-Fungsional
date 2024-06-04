""" def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n>2:
        return fibonacci(n-1)+fibonacci(n-2)
for n in range (1,11):
    print (n, ":", fibonacci(n)) """
fibonacci_cache={}
""" def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    elif n == 1:
        value = 1
    elif n==2:
        value = 1
    elif n>2:
        value = fibonacci(n-1)+fibonacci(n-2)
    fibonacci_cache[n]=value
    return value
for n in range (1,101):
    print (n, ":", fibonacci(n)) """
""" from functools import lru_cache
@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n>2:
        return fibonacci(n-1)+fibonacci(n-2)
for n in range (1,501):
    print (n, ":", fibonacci(n))  """
from functools import lru_cache
""" @lru_cache(maxsize=1000)
def fibonacci(n):
    if type(n)!=int:
        raise TypeError("n harus bilangan integer positif")
    if n<1:
        raise ValueError("n harus bilangan integer posistif")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n>2:
        return fibonacci(n-1)+fibonacci(n-2)
for n in range (1,501):
    print (n, ":", fibonacci(n))  """
""" from functools import partial
def func_multiply(x,y):
    return x*y

print(func_multiply(3,4))
partial_multiply = partial(func_multiply,4)
print (partial_multiply(4))
print(partial_multiply(3)) """
from functools import reduce
data = [2,3,5,7,11,13,17,19,23,29]
multiplier =lambda x,y: x*y
print(reduce (multiplier,data))

product = 1
for x in data :
    product =product * x
print(product)