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