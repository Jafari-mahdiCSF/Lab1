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


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import os
import string
import shutil

# 1. List only directories, only files, and both
def list_directories_files(path):
    print("Directories:")
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    
    print("Files:")
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    
    print("All Entries:")
    print(os.listdir(path))

# 2. Check access: existence, readability, writability, executability
def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

# 3. Test path existence and split into filename and directory
def test_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")

# 4. Count the number of lines in a text file
def count_lines(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    print("Number of lines:", len(lines))

# 5. Write a list to a file
def write_list_to_file(file_path, data):
    with open(file_path, 'w') as f:
        for item in data:
            f.write(f"{item}\n")
    print(f"Written list to {file_path}")

# 6. Generate 26 text files A.txt to Z.txt
def generate_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as f:
            f.write(f"This is file {letter}.txt")
    print("Generated A.txt to Z.txt")

# 7. Copy contents of one file to another
def copy_file(src, dst):
    shutil.copyfile(src, dst)
    print(f"Copied contents from {src} to {dst}")

# 8. Delete file by path with checks
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"{path} deleted successfully.")
    else:
        print(f"Cannot delete {path}. File may not exist or you lack permissions.")

# Example usage
if __name__ == "__main__":
    sample_path = "."  # current directory
    sample_file = "sample.txt"
    sample_copy = "copy_sample.txt"

    print("\n--- List directories and files ---")
    list_directories_files(sample_path)

    print("\n--- Check access to path ---")
    check_access(sample_path)

    print("\n--- Test path existence ---")
    test_path(sample_file)

    print("\n--- Write list to file ---")
    write_list_to_file(sample_file, ["Apple", "Banana", "Cherry"])

    print("\n--- Count lines in file ---")
    count_lines(sample_file)

    print("\n--- Copy file ---")
    copy_file(sample_file, sample_copy)

    print("\n--- Generate alphabet files ---")
    generate_alphabet_files()

    print("\n--- Delete file ---")
    delete_file(sample_copy)

