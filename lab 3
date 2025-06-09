# 1. Define a class which has at least two methods:
#    - getString: to get a string from console input
#    - printString: to print the string in upper case
class StringProcessor:
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())


# 2. Define a class named Shape and its subclass Square.
#    - The Square class has an init function which takes a length as argument.
#    - Both classes have an area function.
#    - Shape's area is 0 by default.
class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length * self.length)


# 3. Define a class named Rectangle which inherits from Shape class from task 2.
#    - Class instance can be constructed by a length and width.
#    - The Rectangle class has a method which can compute the area.
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)


# 4. Write the definition of a Point class.
#    - a method show to display the coordinates of the point
#    - a method move to change these coordinates
#    - a method dist that computes the distance between 2 points
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print((self.x, self.y))
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, p):
        print(math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2))


# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
#    - Withdrawals may not exceed the available balance.
#    - Instantiate your class, make several deposits and withdrawals,
#    - Test to make sure the account can't be overdrawn.
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")


# 6. Write a program which can filter prime numbers in a list by using filter function.
#    Note: Use lambda to define anonymous functions.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_nums = list(filter(lambda x: is_prime(x), nums))
print(prime_nums)

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 1. A recipe you are reading states how many grams you need for the ingredient.
#    Unfortunately, your store only sells items in ounces.
#    Create a function to convert grams to ounces.
#    ounces = 28.3495231 * grams
def grams_to_ounces(grams):
    return grams * 28.3495231


# 2. Read in a Fahrenheit temperature.
#    Calculate and display the equivalent centigrade temperature.
#    C = (5 / 9) * (F – 32)
def fahrenheit_to_centigrade(f):
    return (5 / 9) * (f - 32)


# 3. Classic puzzle: 35 heads and 94 legs among the chickens and rabbits.
#    Create function: solve(numheads, numlegs)
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None


# 4. Write a function filter_prime which will take list of numbers as an argument
#    and returns only prime numbers from the list.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [x for x in numbers if is_prime(x)]


# 5. Write a function that accepts string from user and print all permutations of that string.
import itertools
def print_permutations(s):
    perms = itertools.permutations(s)
    for p in perms:
        print(''.join(p))


# 6. Write a function that accepts string from user, return a sentence with the words reversed.
#    "We are ready" -> "ready are We"
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])


# 7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#    has_33([1, 3, 3]) → True
#    has_33([1, 3, 1, 3]) → False
#    has_33([3, 1, 3]) → False
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


# 8. Write a function that takes in a list of integers and returns True if it contains 007 in order
#    spy_game([1,2,4,0,0,7,5]) --> True
#    spy_game([1,0,2,4,0,5,7]) --> True
#    spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(nums):
    code = [0, 0, 7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if not code:
            return True
    return False


# 9. Write a function that computes the volume of a sphere given its radius.
#    Volume = (4/3) * π * r³
import math
def sphere_volume(r):
    return (4/3) * math.pi * (r**3)


# 10. Write a Python function that takes a list and returns a new list with unique elements.
#     Note: don't use collection set.
def unique_list(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result


# 11. Write a Python function that checks whether a word or phrase is palindrome or not.
#     e.g., madam
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


# 12. Define a function histogram() that takes a list of integers and prints a histogram.
#     histogram([4, 9, 7]) should print:
#     ****
#     *********
#     *******
def histogram(lst):
    for n in lst:
        print('*' * n)


# 13. Write a program able to play the "Guess the number" game.
#     Random number between 1 and 20.
import random
def guess_the_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break


# 14. Create a python file and import some of the functions from the above 13 tasks and try to use them.
#     Example of usage (You can use this in another file):
if __name__ == "__main__":
    print(grams_to_ounces(100))
    print(fahrenheit_to_centigrade(98))
    print(solve(35, 94))
    print(filter_prime([1, 3, 4, 5, 6, 7, 9, 11]))
    print(reverse_words("We are ready"))
    print(has_33([1, 3, 3]))
    print(spy_game([1, 0, 2, 4, 0, 5, 7]))
    print(sphere_volume(3))
    print(unique_list([1, 2, 2, 3, 4, 4, 4, 5]))
    print(is_palindrome("madam"))
    histogram([4, 9, 7])
    # guess_the_number()  # Uncomment to play

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Movie dataset
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# 1. Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def is_high_score(movie):
    return movie["imdb"] > 5.5

# 2. Write a function that returns a sublist of movies with an IMDB score above 5.5.
def get_high_score_movies(movie_list):
    return [movie for movie in movie_list if movie["imdb"] > 5.5]

# 3. Write a function that takes a category name and returns just those movies under that category.
def get_movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"] == category]

# 4. Write a function that takes a list of movies and computes the average IMDB score.
def average_imdb(movie_list):
    if not movie_list:
        return 0
    total = sum(movie["imdb"] for movie in movie_list)
    return total / len(movie_list)

# 5. Write a function that takes a category and computes the average IMDB score.
def average_imdb_by_category(movie_list, category):
    filtered = get_movies_by_category(movie_list, category)
    return average_imdb(filtered)

# Example usage (optional)
if __name__ == "__main__":
    print(is_high_score(movies[0]))  # True
    print(get_high_score_movies(movies))  # List of movies with IMDB > 5.5
    print(get_movies_by_category(movies, "Romance"))  # All Romance category movies
    print(average_imdb(movies))  # Average score of all movies
    print(average_imdb_by_category(movies, "Romance"))  # Average score of Romance movies

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Examples from the w3schools :
def my_function():
  print("Hello from a function")

def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#######################################
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#######################################
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#######################################
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#######################################
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#######################################
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#######################################
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
#######################################
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
#######################################
def myfunction():
  pass
#######################################
def my_function(x, /):
  print(x)

my_function(3)
#######################################
def my_function(x):
  print(x)

my_function(x = 3)
#######################################
def my_function(*, x):
  print(x)

my_function(x = 3)
#######################################
def my_function(x):
  print(x)

my_function(3)
#######################################
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
#######################################
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
############################################## Python Lambda ###############################################################
x = lambda a : a + 10
print(x(5))
#######################################
x = lambda a, b : a * b
print(x(5, 6))
#######################################
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#######################################
def myfunc(n):
  return lambda a : a * n
#######################################
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
#######################################
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
##############################################Python Classes and Objects ####################################################
class MyClass:
  x = 5
#######################################
p1 = MyClass()
print(p1.x)
#######################################
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#######################################
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
#######################################
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
#######################################
Example
Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#######################################
Example
Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
#######################################
Example
Set the age of p1 to 40:

p1.age = 40
#######################################
Example
Delete the age property from the p1 object:

del p1.age
#######################################
Example
Delete the p1 object:

del p1
#######################################
class Person:
  pass
#######################################
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
#######################################
class Student(Person):
  pass
#######################################

x = Student("Mike", "Olsen")
x.printname()
#######################################
Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
#######################################
    #add properties etc.
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
#######################################
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
#######################################
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
#######################################
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
#######################################
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)




