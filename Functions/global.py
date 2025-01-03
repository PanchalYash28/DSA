""" Python Global Keyword"""
# In Python, the global keyword allows us to modify the variable outside of the current scope.
# global variable
c = 1 
def add():
     # increment c by 2
    c = c + 2
    print(c)
add() 
# UnboundLocalError: local variable 'c' referenced before assignment

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




""" What is __name__ in Python? """

# The __name__ variable is a special builtin Python variable that shows the name of the current module.




""" Python Modules"""

""" Import Python Standard Library Modules"""

# import standard math module 
import math

# use math.pi to get value of pi
print("The value of pi is", math.pi)
# The value of pi is 3.141592653589793

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

""" The dir() built-in function"""
print(dir(example))

['__builtins__',
'__cached__',
'__doc__',
'__file__',
'__initializing__',
'__loader__',
'__name__',
'__package__',
'add']
