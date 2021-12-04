'''
SOURCE:
https://docs.python.org/3/library/stdtypes.html
'''


# Text Sequence
# Textual data in Python is handled with str objects, or strings.
# Strings are immutable sequences of Unicode code points.
# String literals are written in a variety of ways:

string_a = 'way_1'
string_b = "way_2"
string_c = '''way_3'''
string_d = """way_4"""

print('\nString Sequence')
print('string_a: {}'.format(string_a))
print('string_b: {}'.format(string_b))
print('string_c: {}'.format(string_c))
print('string_d: {}'.format(string_d))

# methods
capitalized = string_a.capitalize()
print('capitalized version of {} is {}'.format(string_a, capitalized))

casefolded = string_a.casefold()
print('casefolded version of {} is {}'.format(string_a, casefolded))

w = 10
centered = string_a.center(w, '_')
print('centered version of {} is {}'.format(string_a, centered))

char_to_count = 'a'
count = string_a.count(char_to_count)
print('count of {} in the {} is {}'.format(char_to_count, string_a, count))

char_to_end = 'j'
end_with = string_a.endswith(char_to_end)
print('{} is end with {}: {}'.format(string_a, char_to_end, end_with))

char_to_find = 'a'
index_of_found = string_a.find(char_to_find)
print('the 1st index of {} in the {} is {}'.format(char_to_find, string_a, index_of_found))

# index
# Like find(), but raise ValueError when the substring is not found.
# print('the 1st index of {} in the {} is {}'.format(char_to_find, string_a, string_a.index(char_to_find)))

# isalnum()
# Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise.
string_to_check = 'abc123'
print(string_to_check.isalnum())

# isalpha
# Return True if all characters in the string are alphabetic and there is at least one character, False otherwise.
string_to_check = 'abcdef'
print(string_to_check.isalpha())

# isdecimal
# Return True if all characters in the string are decimal characters and there is at least one character, False otherwise.
string_to_check = '012345'
print(string_to_check.isdecimal())

# isdigit
# Return True if all characters in the string are digits and there is at least one character, False otherwise.
string_to_check = '01234'
print(string_to_check.isdigit())

# isidentifier
# Return True if the string is a valid identifier according to the language definition.
from keyword import iskeyword

string_to_check = 'id'
print(string_to_check.isidentifier())
print(iskeyword(string_to_check))

# islower
string_to_check = 'qwert'
print(string_to_check.islower())

# isnumeric
string_to_check = '12345'
print(string_to_check.isnumeric())

# isprintable
string_to_check = 'p09834bg;obiQU32'
print(string_to_check.isprintable())

# isspace
string_to_check = '     '
print(string_to_check.isspace())

# istitle
string_to_check = 'Title'
print(string_to_check.istitle())

# isupper
string_to_check = 'QWERT'
print(string_to_check.isupper())

# join
string_to_joinA = 'qwert'
string_to_joinB = '_____'
string_joined = string_to_joinA.join(string_to_joinB)
print(string_joined)

# ljust
string_to_just = 'qwert'
print(string_to_just.ljust(10, '_'))

# lower
string_to_lower = 'QWERT'
print(string_to_lower.lower())

# lstrip
# Return a copy of the string with leading characters removed.
string_to_strip = 'abcdefghijklmnopqrstuvwxyz'
print(string_to_strip.lstrip('abc'))

# partition
# Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator.
string_to_sep = '12_345'
print(string_to_sep.partition('_'))

# replace
old = 'abababab'
new = 'A'
print(old.replace('a', new, 2))

# split
# Return a list of the words in the string, using sep as the delimiter string.
string_to_split = 'ab_cde_fg'
print(string_to_split.split('_'))

# strip
string_to_strip = '   abc   '
print(string_to_strip.strip())

# swapcase
string_to_swap = 'aBcDeF'
print(string_to_swap.swapcase())

# upper
string_to_upper = 'qwert'
print(string_to_upper.upper())

# zfill
string_to_fill = '1'
print(string_to_fill.zfill(5))
