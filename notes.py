# ======================================================
# PYTHON COMPLETE DEEP DIVE NOTES
# ======================================================
# This file is a one-stop reference for Python basics and core features.
# You can copy this file into VS Code, run snippets, and push it to GitHub.
# ======================================================

# ------------------------------------------------------
# VARIABLES, EXPRESSIONS, STATEMENTS
# ------------------------------------------------------
# Variables: named references to values.
# Expressions: produce a value (e.g., 5 + 3).
# Statements: instructions that do something (e.g., assignments, loops).

x = 10
y = 5 + 3
print(x, y)

# ------------------------------------------------------
# DATA TYPES
# ------------------------------------------------------
# Core built-in types:
# int, float, complex, str, bool, list, tuple, dict, set, NoneType

a = 42             # int
b = 3.14           # float
c = 2 + 3j         # complex
print(c.real, c.imag)    # accessing real and imaginary parts of a complex number
s = "Hello"        # string
flag = True        # bool
nothing = None     # NoneType

# ------------------------------------------------------
# OPERATORS
# ------------------------------------------------------
# Arithmetic: + - * / // % **
# Comparison: == != > < >= <=
# Logical: and or not
# Bitwise: & | ^ ~ << >>
# Identity: is, is not
# Membership: in, not in

print(a.bit_length())    # number of bits required to represent an int

# ------------------------------------------------------
# 'in' vs 'is'
# ------------------------------------------------------
lst = [1, 2, 3]
print(2 in lst)          # membership
print(a is b)            # identity

# ------------------------------------------------------
# STRINGS
# ------------------------------------------------------
text = "Python Programming"
print(text[0:6])         # slicing
print(text[::-1])        # reverse
quote = "She said \"Hello\""
path = "C:\\Users\\Name"

# ------------------------------------------------------
# BOOLEANS
# ------------------------------------------------------
print(bool(0), bool(1), bool(""))

# ------------------------------------------------------
# BUILT-IN FUNCTIONS
# ------------------------------------------------------
# Examples: len(), type(), id(), sum(), max(), min(), sorted(), help(), dir()
nums = [5, 2, 9]
print(len(nums), max(nums), sorted(nums))

# ------------------------------------------------------
# ENUMS
# ------------------------------------------------------
from enum import Enum
class Status(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    DONE = 3

print(Status.PENDING.name, Status.PENDING.value)

# ------------------------------------------------------
# USER INPUT
# ------------------------------------------------------
# name = input("Enter your name: ")
# print("Hello,", name)

# ------------------------------------------------------
# CONTROL STATEMENTS
# ------------------------------------------------------
age = 25
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# ------------------------------------------------------
# LISTS (MUTABLE SEQUENCES)
# ------------------------------------------------------
my_list = [10, 20, 30, 40]

# append: add an element at the end
my_list.append(50)
# extend: add multiple elements (concatenates iterables)
my_list.extend([60, 70])
# insert: insert at a specific index
my_list.insert(1, 15)
# remove: remove first occurrence of a value
my_list.remove(30)
# pop: remove and return element (default last)
popped_value = my_list.pop()
# reverse: reverse the list in place
my_list.reverse()
# index: find the index of a value
idx = my_list.index(20)

print(my_list, popped_value, idx)

# ------------------------------------------------------
# TUPLES (IMMUTABLE SEQUENCES)
# ------------------------------------------------------
coords = (10, 20)
print(coords[0])

# ------------------------------------------------------
# DICTIONARIES (KEY-VALUE MAPPINGS)
# ------------------------------------------------------
person = {"name": "Alice", "age": 30}
print(person.get("age"))      # safe access
person["age"] = 31            # update value
person["city"] = "Paris"      # add new key
print(person)

# ------------------------------------------------------
# SETS (UNORDERED UNIQUE ELEMENTS)
# ------------------------------------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union: elements in A or B
print(A | B)                # or A.union(B)
# Intersection: elements in both A and B
print(A & B)                # or A.intersection(B)
# Difference: elements in A not in B
print(A - B)                # or A.difference(B)
# Subset: check if A is subset of B
print({1, 2}.issubset(A))

# ------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))
print(greet("Alice", greeting="Hi"))

# ------------------------------------------------------
# VARIABLE SCOPE (LEGB)
# ------------------------------------------------------
var = "global"
def scope_example():
    var = "local"
    print("Inside:", var)
scope_example()
print("Outside:", var)

# ------------------------------------------------------
# CLOSURES
# ------------------------------------------------------
def outer(msg):
    def inner():
        return msg
    return inner

fn = outer("Captured")
print(fn())

# ------------------------------------------------------
# LOOPS
# ------------------------------------------------------
for i in range(3):
    print("For loop:", i)

count = 0
while count < 3:
    print("While loop:", count)
    count += 1

# break and continue
for i in range(5):
    if i == 2:
        continue   # skip 2
    if i == 4:
        break      # stop loop
    print("Value:", i)


#---------------------------------------------------
# Classes : type of an object 

class Dog:
    def __init__(self,name,age): #constructor
        self.name = name
        self.age = age

    def bark(self):
       return 'woof!'

roger = Dog('roger', 8)
print(roger.name)
print(roger.age)
print(roger.bark())
        
#inheritance

# here animal is inherited by dog
class Animal:
    def walk(self):
        print('walking....')


class Dog(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
       return 'woof!'

roger = Dog('roger', 8)
print(roger.name)
print(roger.age)
print(roger.bark())
roger.walk()


#--------------------------------------------
#Modules

#dog.py
def bark():
    print('woof')

#main.py
"""import dog # or from dog import bark

dog.bark() #bark()"""

# we can import the components or functions with 'import' keyword
#if the content is inside folder,then create empty file '__init__.py' inside the folder and import the required file 
# more pre defined libraries math,re,json,os,http,random etc.,


"""
Python Notes: sys and argparse Libraries
----------------------------------------

1. sys module
-------------
- The `sys` module provides access to system-specific parameters and functions.
- It is often used to interact with the Python interpreter and command-line arguments.

Common uses:
- sys.argv: A list of command-line arguments passed to the script.
    Example:
        import sys
        print("Script name:", sys.argv[0])
        print("Arguments:", sys.argv[1:])
- sys.exit([code]): Exits the program. You can provide an exit status code (0 for success).
    Example:
        import sys
        if len(sys.argv) < 2:
            print("No arguments provided.")
            sys.exit(1)
- sys.path: A list of directories where Python looks for modules.
    Example:
        import sys
        print(sys.path)
- sys.version: Displays the version of Python being used.

2. argparse module
-------------------
- The `argparse` module makes it easy to write user-friendly command-line interfaces.
- It handles parsing arguments and automatically generates help and usage messages.

Steps to use argparse:
1. Import argparse.
2. Create a parser object using argparse.ArgumentParser().
3. Add arguments using parser.add_argument().
4. Parse the arguments using parser.parse_args().

Basic Example:
    import argparse

    # Step 1: Create parser
    parser = argparse.ArgumentParser(description="Demo of argparse usage.")

    # Step 2: Add arguments
    parser.add_argument("name", help="Your name")
    parser.add_argument("-a", "--age", type=int, help="Your age")

    # Step 3: Parse arguments
    args = parser.parse_args()

    # Step 4: Use the arguments
    print(f"Hello, {args.name}!")
    if args.age:
        print(f"You are {args.age} years old.")

Features:
- Positional arguments: Required arguments (like 'name' in the example).
- Optional arguments: Usually prefixed with '-' or '--' (like '-a' or '--age').
- Automatic help: Running `python script.py --help` shows available options.
- also we can use choices like choices={'red','yellow'}

Summary:
- Use `sys` for simple and low-level command-line argument access.
- Use `argparse` for structured, user-friendly, and maintainable argument parsing.
"""
# lambda 
"""
lambda function
multiply = labmda a,b = a*b


"""
#map(), filter(), reduce()
"""
Python Notes: map(), filter(), and reduce()
-------------------------------------------

1. map(function, iterable)
--------------------------
- Applies a given function to each item in an iterable (like a list, tuple, etc.)
- Returns a map object (an iterator) which can be converted to a list/tuple if needed.

Example:
    numbers = [1, 2, 3, 4, 5]
    def square(x):
        return x * x

    squared = map(square, numbers)
    print(list(squared))   # Output: [1, 4, 9, 16, 25]

Shorter version using lambda:
    squared = map(lambda x: x * x, numbers)
    print(list(squared))

2. filter(function, iterable)
-----------------------------
- Filters items out of an iterable for which the function returns True.
- Only the elements that satisfy the condition are kept.

Example:
    numbers = [10, 15, 20, 25, 30]
    def is_even(x):
        return x % 2 == 0

    evens = filter(is_even, numbers)
    print(list(evens))   # Output: [10, 20, 30]

Using lambda:
    evens = filter(lambda x: x % 2 == 0, numbers)
    print(list(evens))

3. reduce(function, iterable)
-----------------------------
- Applies a rolling computation to sequential pairs of values in the iterable.
- Unlike map and filter, reduce is not built-in by default (it lives in the functools module).

Example:
    from functools import reduce

    numbers = [1, 2, 3, 4, 5]
    def add(x, y):
        return x + y

    total = reduce(add, numbers)
    print(total)   # Output: 15

Using lambda:
    total = reduce(lambda x, y: x + y, numbers)
    print(total)

Summary:
--------
- map   → transform each element
- filter→ keep only elements that meet a condition
- reduce→ combine all elements into a single result
"""


