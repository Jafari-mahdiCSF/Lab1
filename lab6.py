from functools import reduce
import math
import time

# 1. Multiply all the numbers in a list
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

# 2. Count uppercase and lowercase letters in a string
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

# 3. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# 4. Invoke square root function after specific milliseconds
def delayed_sqrt(value, delay_ms):
    time.sleep(delay_ms / 1000.0)  # Convert milliseconds to seconds
    result = math.sqrt(value)
    print(f"Square root of {value} after {delay_ms} miliseconds is {result}")

# 5. Return True if all elements of the tuple are true
def all_true(t):
    return all(t)

# Example usages
if __name__ == "__main__":
    print("Multiply list:", multiply_list([2, 3, 4]))  # 24

    count_case("Hello World!")  # Upper: 2, Lower: 8

    print("Is 'madam' palindrome?:", is_palindrome("madam"))  # True
    print("Is 'hello' palindrome?:", is_palindrome("hello"))  # False

    delayed_sqrt(25100, 2123)  # Will wait and then print square root

    print("All true in tuple?:", all_true((True, True, 1, "non-empty")))  # True
    print("All true in tuple?:", all_true((True, False, 1)))              # False
