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

import re

# -------------------------
# Example 1: Email Extractor
# -------------------------
text = """
Hi there, contact me at john.doe123@gmail.com or at office@company.org. 
You can also try jane-doe@work.net or something@not-an-email.
"""

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net)'
emails = re.findall(email_pattern, text)
# re.findall returns only the domain group by default; to get full emails, use non-capturing group:
email_pattern_fixed = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(?:\.com|\.org|\.net)'
emails = re.findall(email_pattern_fixed, text)

print("Example 1 - Extracted Emails:")
print(emails)

# -------------------------
# Example 2: Log File Cleaner
# -------------------------
log_data = """
192.168.1.1 - - [12/Jun/2023:10:15:32 +0000] "GET /index.html"
10.0.0.2 - - [13/Jun/2023:11:20:55 +0000] "POST /submit"
"""

log_pattern = r'(\d{1,3}(?:\.\d{1,3}){3}) - - \[(\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2})'
log_matches = re.findall(log_pattern, log_data)

print("\nExample 2 - Extracted IP and Timestamps:")
print(log_matches)

# -------------------------
# Example 3: Password Validator
# -------------------------
passwords = ["Welcome123", "abc", "NOLOWERCASE1", "validPass1"]

# At least 8 characters, one lowercase, one uppercase, one digit
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
valid_passwords = [pwd for pwd in passwords if re.fullmatch(password_pattern, pwd)]

print("\nExample 3 - Valid Passwords:")
print(valid_passwords)

# -------------------------
# Example 4: Twitter Hashtag Extractor
# -------------------------
tweets = [
    "Excited about #Python3 🐍 and #AI!",
    "Loving the vibes of #Kazakhstan 🇰🇿 #travel #fun_times"
]

hashtag_pattern = r'#\w+'
all_hashtags = []
for tweet in tweets:
    all_hashtags += re.findall(hashtag_pattern, tweet)

print("\nExample 4 - Extracted Hashtags:")
print(all_hashtags)

# -------------------------
# Example 5: Phone Number Normalizer
# -------------------------
phones = ["+7 701 123 4567", "87011234567", "7-701-123-45-67"]
normalized_phones = []

for phone in phones:
    digits = re.findall(r'\d', phone)
    if len(digits) == 11:
        normalized = f"+7 ({''.join(digits[1:4])}) {''.join(digits[4:7])}-{''.join(digits[7:9])}-{''.join(digits[9:11])}"
        normalized_phones.append(normalized)

print("\nExample 5 - Normalized Phone Numbers:")
print(normalized_phones)

