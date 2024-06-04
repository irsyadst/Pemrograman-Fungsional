""" def lowercase(func):
    def wrapper():
        func_ret = func()
        change_to_lowecase = func_ret.lower()
        return change_to_lowecase
    return wrapper
def hello_function():
    return'HELLO WORLD!'
decorate = lowercase((hello_function))
print(decorate())
def split_sentence(func):
    def wrapper():
        func_ret = func()
        output = func_ret.split()
        return output
    return wrapper
@split_sentence
@lowercase
def hello_function():
    return 'HELLO WORLD!'
print(hello_function) """
""" import functools
def memoize(function):
    function.cache = dict()
    @function.wraps(function)
    def _memoize(*args):
        if args not in function.cache:
            function.cache[args] = function(*args)
            return function.cache[args]
        return _memoize
    @memoize
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
        for i in range(1, 7):
            print('fibonacci %d: %d' % (i, fibonacci(i))) """
import functools
def counter(function):
    function.calls = 0
    @functools.wraps(function)
    def _counter(*args, **kwargs):
        function.calls += 1
        return function(*args, **kwargs)
    return _counter
