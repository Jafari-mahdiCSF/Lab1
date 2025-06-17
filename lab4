# 1. Python Iterators and Generators
# 1.1. Create an iterator that prints each element from the list [10, 20, 30, 40] using iter() and next().

my_list = [10, 20, 30, 40]
my_iterator = iter(my_list)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# 2. Python Scope
# 2.1. Create a function with a local variable x = 5, and print x both inside and outside the function. Show the difference between local and global scope.

def local_scope():
    x = 5
    print("Inside function, x =", x)

local_scope()
try:
    print("Outside function, x =", x)
except NameError:
    print("Outside function, x is not defined (NameError)")

# 2.2. Use the global keyword inside a function to modify a global variable.

y = 10

def modify_global():
    global y
    y = 20

modify_global()
print("Global y after modification:", y)

# 3. Python Modules
# 3.1. Create a module math_utils.py with a function add(a, b). Import and call this function in a main file.
# Simulating the module inside this file for simplicity.

def add(a, b):
    return a + b

print("Sum using math_utils module function:", add(5, 7))

# 3.2. Import the random module and write a program that prints a random number between 1 and 100.

import random
print("Random number between 1 and 100:", random.randint(1, 100))

# 4. Python Dates
# 4.1. Print today's date in DD-MM-YYYY format using strftime().

from datetime import date
print("Today's date:", date.today().strftime("%d-%m-%Y"))

# 4.2. Calculate how many days are left until your next birthday.
from datetime import datetime

today = datetime.now()
next_birthday = datetime(today.year, 12, 25)  # change to your birthday
if today > next_birthday:
    next_birthday = datetime(today.year + 1, 12, 25)
days_left = (next_birthday - today).days
print("Days until next birthday:", days_left)

# 5. Python Math
# 5.1. Using the math module, find the square root of 81, value of pi, and round down 5.9.

import math
print("Square root of 81:", math.sqrt(81))
print("Value of pi:", math.pi)
print("Rounded down 5.9:", math.floor(5.9))

# 5.2. Calculate the area of a circle with radius r using the formula π * r^2.

r = 3
area = math.pi * r ** 2
print("Area of a circle with radius 3:", area)

# 6. Python JSON
# 6.1. Create a dictionary with student data (name, age, GPA) and convert it to JSON using json.dumps().

import json
student = {"name": "Ali", "age": 20, "GPA": 3.8}
student_json = json.dumps(student)
print("Student JSON:", student_json)

# 6.2. Parse the JSON string {"course": "Python", "level": "beginner"} and get the value for the key course.

json_string = '{"course": "Python", "level": "beginner"}'
parsed_data = json.loads(json_string)
print("Course value:", parsed_data["course"])
