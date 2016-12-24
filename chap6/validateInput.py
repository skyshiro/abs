# can use a backslash infront of characters for special characters
# \' for single quote
# \t for tab
# \\ for backlash

# use r before string to make raw string. ignores escape characters
# r'Carol\'s cat' -> Carol\'s cat

# multiline strings with triple quotes '''string'''

""" Multiline comments use triple pound
test
test
test

strings have indexing and slicing like lists

can use "in" and "not in" with strings like lists
"hello" in "hello world" -> True

upper() and lower() to change case of string
test = 'test'
test.upper() -> TEST

isupper() and islower() returns boolean

various other isX():
isalpha() - only letters and not blank
isalnum() - only letters and numbers and not blank
isdecimal() - only numberse and not blank
isspace() - only spaces, tabs, and new lines and not blank

startswith('string') and endswith('string') easy way to see if
string begins or end with string passed

join() called on a list of strings
', '.join(['a', 'b', 'c']) -> 'a, b, c'

split() call on a separator. can call split on \n
'a, b, c'.split(', ') = ['a', 'b', 'c']

justify text with rjust(), ljust() and center() methods
'hello'.rjust(10) -> '     hello'
    -can fill space with other character.
    -string.ljust(10, '*')

remove white space with strip(), lstrip() and rstrip()

copy and paste strings from clipboard with pyperclip!
"""

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords are alphanumeric')
