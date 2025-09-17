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

#--------------------------------------------
#Collections
#counter 
"""
it counts the frequencies of each letters in a string in the form of key value pair
from collections import Counter
a = 'aaabbbccaabdbbbcccc'
my_counter= Counter(a)
print(my_counter)
print(my_counter.values())
print(my_counter.items())
print(my_counter.keys())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

"""

#namedtuple
"""
similar to structure
from collections import namedtuple
point = namedtuple('point','x,y')
pt = point(1,-4)
print(pt)
print(pt.x, pt.y)

"""
#Orderdictionary
"""
from collections import OrderedDict
Order = {}
Order['a'] = 1
Order['c']=3
Order['d']=4
Order['b']=2
print(Order)
"""

#defaultdict
"""from collections import defaultdict
d = defaultdict(int)
d['a']=1
d['b']=2
print(d['c']) #return default value 0"""

#deque
"""double ended queue
from collections import deque
d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d.extend([4,5,6])
print(d)

d.rotate(1)
print(d)"""

#------------------------------------------
#itertools
#product
"""it iterates and combines and makes pairs in the given list
from itertools import product
a=[1,2]
b=[3,4]
prod = product(a,b, repeat=2)
print(list(prod))"""

#permutations
"""from itertools import permutations
a=[1,2,3]

prod = permutations(a,2)
print(list(prod))"""

#combinations
"""
from itertools import combinations, combinations_with_replacement
a=[1,2,3]

prod = combinations(a,2)
print(list(prod))

comb = combinations_with_replacement(a,2)
print(list(comb))"""

#accumulate
""" calculates accumulate value
from itertools import accumulate
import operator
a=[1,2,3,4,2]

prod = accumulate(a)
print(a)
print(list(prod))

multiply = accumulate(a, func=operator.mul)
print(list(multiply))

maximum = accumulate(a, func=max)
print(list(maximum))
"""

#groupby
"""from itertools import groupby


a =[1,2,3,4]
group = groupby(a,key=lambda x : x<3)
for key, value in group:
    print(key, list(value))
person = [{'name':'tim','age':25},{'name':'a','age':20},{'name':'tim','age':35},{'name':'tim','age':45}]
group_obj = groupby(person,key=lambda x:x['age'])

for key, value in group_obj:
    print(key, list(value))
"""
#---------------------------------------------------------
#Errors and Exceptions
""" Asserts, exceptions and try catch block
raising exception:
x = -5
if x < 0:
    raise Exception('x should be positive')
Assertion:
    x = -5
assert (x>0), ' x is not positive'

try and exception:
try:
    a = 5 /0
except:
    print('invalid syntax')

To fine what type of error:
try:
    a = 5 /0
except Exception as e:
    print(e)

Multiple correction:
try:
    a=5/1
    b=a+4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up..........')

defining own error:
class ValueError(Exception):
    pass

def test_value(x):
    if x>100:
        raise ValueError('Value is too high')

try:    
    test_value(200)
except ValueError as e:
    print(e)
"""

# ================================================
#      🐍 PYTHON LOGGING – QUICK REFERENCE
# ================================================

"""
LOGGING = Recording events while a program runs.
Provides better control than print() for debugging and monitoring.
"""

# ------------------------------
# 1. IMPORT LOGGING
# ------------------------------
import logging

# ------------------------------
# 2. BASIC CONFIGURATION
# ------------------------------
logging.basicConfig(
    level=logging.DEBUG,                         # Minimum level to log
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

# Example logs:
logging.debug("Debugging details")
logging.info("Application started")
logging.warning("Something might be wrong")
logging.error("An error occurred")
logging.critical("Critical failure")

# ------------------------------
# 3. LOGGING LEVELS
# ------------------------------
"""
Levels (by importance):
    DEBUG    : Detailed info (value checking, step-by-step)
    INFO     : General info about program flow
    WARNING  : Something unexpected but program continues
    ERROR    : A serious problem; function failed
    CRITICAL : Very serious error; program may not continue
"""

# ------------------------------
# 4. LOGGING TO A FILE
# ------------------------------
logging.basicConfig(
    filename='app.log',                          # Save logs to file
    level=logging.INFO,                          # Minimum level to log
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Program started")
logging.warning("Low disk space")
logging.error("File not found")

# ------------------------------
# 5. FORMAT PLACEHOLDERS
# ------------------------------
"""
Common placeholders for format strings:

    %(asctime)s   : Date & time of log
    %(levelname)s : Log level (INFO, ERROR, etc.)
    %(message)s   : The log message text
    %(name)s      : Logger name
    %(filename)s  : File name where log was created
    %(lineno)d    : Line number
    %(threadName)s: Thread name
    %(process)d   : Process ID
"""

# Example advanced format:
logging.basicConfig(
    format='%(asctime)s | %(name)s | %(filename)s:%(lineno)d | %(levelname)s | %(message)s'
)

# ------------------------------
# 6. CUSTOM LOGGER (ADVANCED)
# ------------------------------
# Create a custom logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler("my_app.log")

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(file_handler)

# Use custom logger
logger.info("Application initialized")
logger.error("Something went wrong")

# ================================================
#            END OF PYTHON LOGGING NOTES
# ================================================


#-----------------------------------------------
#JSON
"""
Python                                                              JSON
dict                                                                object
list,tuple                                                          array
str                                                                 str
int, long, float                                                    number
True                                                                true
False                                                               false
None                                                                null
"""

""" convert python object to json
import json
person = {
    "name":"john",
    "age":30,
    "city":"India",         ---------------------->python object
    "haschildren":False,
    "titles":["engineer", "programmer"]
}

personJson = json.dumps(person, indent=4, separators=(': ','= '), sort_keys=True) ---------> json conversion
print(personJson)


with open('person.json', 'w') as file: 
    json.dump(person, file, indent=4)--------------------> stores data in .json file"""


""" json to python
person = json.loads(personJson)
print(person)

with open('person.json', 'r') as file:
    person=json.load(file)
    print(person)"""

#---------------------------------------------------
#Random 
""" random.random() ---> random no. from 0 to 1
random.uniform(a,b) ---> random no. from a to b float
random.randint(a,b)----> integer b/w a to b
random.randrange(a,b)----> random int without including b
random.normalvariate(a,b)---->for statiscts
random.choice(list_name)---> chooses any random element from list
random.sample(list,n)----> choses any n elements in the list
random.choices(list, k= )---->allows single element multiple times
random.suffle(list)---> shuffles the list
random.seed(n)---> to get the same random values in many places


to generate passwords we use secret instead of random because of security
import secrets
secret.randbelow(a)---->generates random no. without includng a
secret.randbit(a)---->creates a bit number
secrets.choice(list)


numpy:
import numpy as np
np.random.randint(a,b)--->creates array of 3 * 4
np.random.shuffle(). np.random.seed(1)"""

#-----------------------------------------------
#decorators
"""ex: 1 def dosomething(func):
    def sum(*args, **kwargs):
        print('before')
        res = func(*args, **kwargs)
        print('after')
        return res
    return sum

@dosomething
def add(x):
    return x+5

result = add(5)
print(result)
print(help(result))
-----------------------------
 ex:2 import functools
def repeat(numtimes):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(numtimes):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator



@repeat(numtimes = 4)
def greet(name):
    print("hello "+ name)

greet('nitya')



"""
#------------------------------
#generator
"""A generator is a special kind of iterator in Python.

Instead of returning all values at once (like a list), it yields values one at a time, only when needed.

This makes them memory efficient and perfect for working with large datasets or infinite sequences.

def count_up_to(n):
    i = 1
    while i <= n:
        yield i   # pauses & returns a value
        i += 1

gen = count_up_to(5)
print(next(gen))  # 1
print(next(gen))  # 2
print(list(gen))  # [3, 4, 5]
"""

#----------------------------------
#multithreading
"""from threading import Thread,Lock

import time

database_value = 0
def increase(lock):
    global database_value
    lock.acquire()
    local_copy = database_value
    local_copy+= 1
    time.sleep(0.1)
    database_value = local_copy
    lock.release()

if __name__ == "__main__":
    lock = Lock()
    print('start value', database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase,  args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)
    -----------------------------
    
    queues in multithreading
    from threading import Thread,Lock
from queue import Queue
import time



if __name__ == "__main__":
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)

    first = q.get()
    print(first)
    
    q.task_done()
    q.join()
    print('end value')
    
    ------------------------
    from threading import Thread,Lock, current_thread
from queue import Queue
import time

def worker(q):
    while True:
        value = q.get()
    # processing....
        print(f'in {current_thread().name} got {value}')
        q.task_done()



if __name__ == "__main__":
    q = Queue()
    
    
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,))
        thread.daemon = True #to prevent infinite loop
        thread.start()

    for i in range(1,21):
        q.put(i)

    q.join()

    print('end main')
"""
