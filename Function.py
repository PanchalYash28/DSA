""" Python Functions """
# -  A function is a block of code that performs a specific task.

# Suppose we need to create a program to make a circle and color it. We can create two functions to solve this problem:

# function to create a circle
# function to color the shape
# Dividing a complex problem into smaller chunks makes our program easy to understand and reuse.

""" Example: Create a function"""

def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')

""" Note: When writing a function, pay attention to indentation, which are the spaces at the start of a code line.
In the above code, the print() statement is indented to show it's part of the function body, distinguishing the function's definition from its body.""" 


""" Example: Python Function Call """

def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')


""" Ex: 3 Python Function Arguments """

def greet(name):
    print("Hello", name)

# pass argument
greet("John")

""" Example: Function to Add Two Numbers """

# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)


"""" Parameter vs Arguments"""

def print_age(age):  # age is a parameter
    print(age)

print_age(25)  # 25 is an argument



""" Pass statement"""

def future_function():
    pass

# this will execute without any action or error
future_function()  



""" Python Library Functions"""
# 1. print() - prints the string inside the quotation marks
# 2. sqrt() - returns the square root of a number
# 3. pow() - returns the power of a number


""" Example: Python Library Function """
import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)

""" User Defined Vs Standard Library Functions """
# In Python, functions are divided into two categories: user-defined functions and standard library functions. These two differ in several ways:

# User-Defined Functions

# These are the functions we create ourselves. They're like our custom tools, designed for specific tasks we have in mind.

# They're not part of Python's standard toolbox, which means we have the freedom to tailor them exactly to our needs, adding a personal touch to our code.

# Standard Library Functions

# Think of these as Python's pre-packaged gifts. They come built-in with Python, ready to use.

# These functions cover a wide range of common tasks such as mathematics, file operations, working with strings, etc.



""" Default Arguments in Functions """
# Python allows functions to have default argument values. 
# Default arguments are used when no explicit values are passed to these parameters during a function call.

def greet(name, message="Hello"):
    print(message, name)

# calling function with both arguments
greet("Alice", "Good Morning")

# calling function with only one argument
greet("Bob")


""" Using *args and **kwargs in Functions """
# We can handle an arbitrary number of arguments using special symbols *args and **kwargs.

# *args in Functions
# Using *args allows a function to take any number of positional arguments.
# function to sum any number of arguments

def add_all(*numbers):
    return sum(numbers)

# pass any number of arguments
print(add_all(1, 2, 3, 4))   


# Using **kwargs allows the function to accept any number of keyword arguments.

# function to print keyword arguments
def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")

# pass any number of keyword arguments
greet(name="John", greeting="Hello")
