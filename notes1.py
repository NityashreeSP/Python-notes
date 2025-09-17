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
