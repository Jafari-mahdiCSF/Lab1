import re

# 1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
def match_a_followed_by_zero_or_more_b(s):
    return re.fullmatch(r"ab*", s) is not None

# 2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
def match_a_followed_by_2_to_3_b(s):
    return re.fullmatch(r"ab{2,3}", s) is not None

# 3. Write a Python program to find sequences of lowercase letters joined with an underscore.
def find_lowercase_joined_with_underscore(s):
    return re.findall(r"[a-z]+_[a-z]+", s)

# 4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def find_upper_followed_by_lower(s):
    return re.findall(r"[A-Z][a-z]+", s)

# 5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def match_a_anything_ending_in_b(s):
    return re.fullmatch(r"a.*b", s) is not None

# 6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def replace_with_colon(s):
    return re.sub(r"[ ,.]", ":", s)

# 7. Write a python program to convert snake case string to camel case string.
def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)

# 8. Write a Python program to split a string at uppercase letters.
def split_at_uppercase(s):
    return re.findall(r'[A-Z][^A-Z]*', s)

# 9. Write a Python program to insert spaces between words starting with capital letters.
def insert_spaces_before_capitals(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

# 10. Write a Python program to convert a given camel case string to snake case.
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

# ----------------- Test Cases -----------------
if __name__ == "__main__":
    print(match_a_followed_by_zero_or_more_b("abbb"))          # True
    print(match_a_followed_by_2_to_3_b("abb"))                 # True
    print(find_lowercase_joined_with_underscore("this_is_a_test_case"))  # ['this_is', 'a_test']
    print(find_upper_followed_by_lower("HelloWorld TEST test"))          # ['Hello', 'World', 'Test']
    print(match_a_anything_ending_in_b("a123b"))               # True
    print(replace_with_colon("Hi, how are you. I am fine"))    # 'Hi::how:are:you::I:am:fine'
    print(snake_to_camel("hello_world_test"))                  # 'helloWorldTest'
    print(split_at_uppercase("SplitAtUpperCaseLetters"))       # ['Split', 'At', 'Upper', 'Case', 'Letters']
    print(insert_spaces_before_capitals("AddSpaceBeforeCapsNow")) # 'Add Space Before Caps Now'
    print(camel_to_snake("ConvertThisToSnakeCase"))            # 'convert_this_to_snake_case'
# PRACTICE QUESIONS :
