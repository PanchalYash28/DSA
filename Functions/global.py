""" Python Global Keyword"""
# In Python, the global keyword allows us to modify the variable outside of the current scope.
# global variable
c = 1 
def add():
     # increment c by 2
    c = c + 2
    print(c)
add() 
# Output: UnboundLocalError: local variable 'c' referenced before assignment

""" Example: Changing Global Variable From Inside a Function using global"""

# global variable
c = 1 
def add():
    # use of global keyword
    global c
    # increment c by 2
    c = c + 2 
    print(c)
add()
# Output: 3


""" What is __name__ in Python? """

# The __name__ variable is a special builtin Python variable that shows the name of the current module.


""" Python Modules"""

""" Import Python Standard Library Modules"""

# import standard math module 
import math

# use math.pi to get value of pi
print("The value of pi is", math.pi)
# Output: The value of pi is 3.141592653589793

""" Python import with Renaming """
# import module by renaming it
import math as m

print(m.pi)
# Output: 3.141592653589793

"""" Python from...import statement"""
# import only pi from math module
from math import pi

print(pi)
# Output: 3.141592653589793

""" Import all names """
# import all names from the standard module math
from math import *

print("The value of pi is", pi)
# Output: The value of pi is 3.141592653589793

""" The dir() built-in function"""
print(dir())
# Output:
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__',
 '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil',
 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2',
 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot',
 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log',
 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians',
 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'traceback', 'trunc', 'ulp']
