'''
This file contains most of the types in the source website.
For more classified version, see 02_NUM_builtin_types_TOPIC.py

SOURCE:
https://docs.python.org/3/library/stdtypes.html
'''


# Truth Value Testing
# Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below.

print('\nTruth Value Testing is "if" and "while"')

# constants defined to be false: None and False.
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '', (), [], {}, set(), range(0)

object_to_test = None
# object_to_test = False
# object_to_test = True
# object_to_test = 0
# object_to_test = 1
# object_to_test = []
# object_to_test = 'text'

if object_to_test:
    print('{} is considered as True'.format(object_to_test))
else:
    print('{} is considered as False'.format(object_to_test))



# Boolean Operations

print('\nBoolean Operations is "or", "and" and "not"')

# This is a short-circuit operator, so it only evaluates the second argument if the first one is false.
# This is a short-circuit operator, so it only evaluates the second argument if the first one is true.
# not has a lower priority than non-Boolean operators, so not a == b is interpreted as not (a == b), and a == not b is a syntax error.

x = True
y = False

if x or y:
    print('one of the x or y is True')

if x and y:
    print('both x and y are True')

if not x:
    print('x is False')
else:
    print('x is True')



# Comparisons
print('\nComparisons are "<", "<=," ">", ">=," "==," "!=," "is" and "is not"')

value_a = 1
reference = 0

comparison = value_a < reference
print('comparison "{} < {}" returns {}'.format(value_a, reference, comparison))

comparison = value_a <= reference
print('comparison "{} <= {}" returns {}'.format(value_a, reference, comparison))

comparison = value_a > reference
print('comparison "{} > {}" returns {}'.format(value_a, reference, comparison))

comparison = value_a >= reference
print('comparison "{} >= {}" returns {}'.format(value_a, reference, comparison))

comparison = value_a == reference
print('comparison "{} == {}" returns {}'.format(value_a, reference, comparison))

comparison = value_a != reference
print('comparison "{} != {}" returns {}'.format(value_a, reference, comparison))

comparison = value_a is reference
print('comparison "{} is {}" returns {}'.format(value_a, reference, comparison))

comparison = value_a is not reference
print('comparison "{} is not {}" returns {}'.format(value_a, reference, comparison))




# Numeric
# There are three distinct numeric types: integers, floating point numbers, and complex numbers.
print('\nNumeric Types are "int", "float" and "complex"')

original_num = 0

integer = int(original_num)
floating_point_num = float(original_num)
complex_num = complex(original_num)

print('integer of {} is {}'.format(original_num, integer))
print('floating point number of {} is {}'.format(original_num, floating_point_num))
print('compex number of {} is {}'.format(original_num, complex_num))

# Operations

x = 2
y = 3

# +
addition = x + y
print('sum of {} and {} is {}'.format(x, y, addition))

# -
difference = x - y
print('difference of {} and {} is {}'.format(x, y, difference))

# *
product = x + y
print('product of {} and {} is {}'.format(x, y, product))

# /
quotient = x + y
print('quotient of {} and {} is {}'.format(x, y, quotient))

# //
floored_quotient = x + y
print('floored_quotient of {} and {} is {}'.format(x, y, floored_quotient))

# %
remainder = x + y
print('remainder of {} and {} is {}'.format(x, y, remainder))

# -x
negated = -x
print('negated of {} is {}'.format(x, negated))

# +
unchanged = +x
print('unchanged of {} is {}'.format(x, unchanged))

# **
powers = x ** y
print('{} to the power {} is {}'.format(x, y, powers))

# methods
a_float =  -2.0
print('{} is finite with integral value: {}'.format(a_float, float(a_float).is_integer()))



# Iterator



# Sequence
# There are three basic sequence types: lists, tuples, and range objects.
# Additional sequence types tailored for processing of binary data and text strings are described in dedicated sections.

sequence_list = list([i for i in range(10)])
sequence_tuple = tuple((i for i in range(10)))
sequence_range = range(10)

print('\nSequence')
print('list: {}'.format(sequence_list))
print('tuple: {}'.format(sequence_tuple))
print('range: {}'.format(sequence_range))

# operations

item_to_check = -1

# in
if item_to_check in sequence_list:
    print('{} is in the list'.format(item_to_check))
else:
    print('{} is NOT in the list'.format(item_to_check))

# not in
if item_to_check not in sequence_list:
    print('{} is NOT in the list'.format(item_to_check))
else:
    print('{} is in the list'.format(item_to_check))

# +
list_a = list([i for i in range(10)])
list_b = list([i*10 for i in range(10)])
concatenated = list_a + list_b
print('concatenated list is {}'.format(concatenated))

# *
multiplied = list_a * 2
print('multiplied is {}'.format(multiplied))

# slicing
index = 0
item_at_index = list_a[index]
print('{}th index in the {} is {}'.format(index, list_a, item_at_index))

start_ind = 2
end_ind = 6
sliced_list = list_a[start_ind:end_ind]
print('{} is extracted from {}th to {}th index of the {}'.format(sliced_list, start_ind, end_ind-1, list_a))

step = 2
sliced_list = list_a[start_ind:end_ind:step]
print('{} is every {}th items from {}th to {}th index of the {}'.format(sliced_list, step, start_ind, end_ind-1, list_a))

# muting
replacement = 100
index_to_replace = 3
list_a[index_to_replace] = replacement
print(list_a)

replacement = list([i*100 for i in range(1, 4)])
start_index_to_replace = 3
end_index_to_replace = 6
list_a[start_index_to_replace:end_index_to_replace] = replacement
print(list_a)

start_index_to_delete = 3
end_index_to_delete = 6
del list_a[start_index_to_delete:end_index_to_delete]
print(list_a)

times_to_repeat = 3
list_a *= times_to_repeat
print(list_a)



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



# Binary Sequence
# Bytes objects are immutable sequences of single bytes.
# Since many major binary protocols are based on the ASCII text encoding,
# bytes objects offer several methods that are only valid when working with ASCII compatible data and are closely related to string objects in a variety of other ways.



# Set
# A set object is an unordered collection of distinct hashable objects.
# Common uses include membership testing,
#                     removing duplicates from a sequence and
#                     computing mathematical operations such as intersection, union, difference, and symmetric difference.



# Mapping = dict

# multiple ways of defining a dictionary

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(a == b == c == d == e == f)

# dictionary related methods

# list
# Return a list of all the keys used in the dictionary d.
print(list(d))

# len
# Return the number of items in the dictionary d.
print(len(d))

# d[key]
# Return the item of d with key key. Raises a KeyError if key is not in the map.
print(d['one'])

# d[key] = value
# Set d[key] to value.
d['one'] = 1.0
print(d['one'])

# del d[key]
# Remove d[key] from d. Raises a KeyError if key is not in the map.
del d['one']
print(d)

# key in d
# Return True if d has a key key, else False.
key_to_check = 'four'
print(key_to_check in d)

# key not in d
# Equivalent to not key in d.
print(key_to_check not in d)

# iter
# Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys()).
iterator = iter(d)
print(iterator)
print(iterator.__next__())
print(iterator.__next__())
# print(iterator.__next__()) this will be out of range

# clear()
# Remove all items from the dictionary.
d.clear()
print(d)

# copy
# Return a shallow copy of the dictionary.
a_copied = a.copy()
print(a_copied)

# get
# Return the value for key if key is in the dictionary, else default.
# If default is not given, it defaults to None, so that this method never raises a KeyError.
value_to_get = a.get('one')
print(value_to_get)

# items
# Return a new view of the dictionary’s items ((key, value) pairs).
view = a.items()
print(view)

# keys
# Return a new view of the dictionary’s keys
view = a.keys()
print(view)

# pop
# If key is in the dictionary, remove it and return its value, else return default.
# If default is not given and key is not in the dictionary, a KeyError is raised.
a.pop('one')
print(a)

# popitem
popped = a.popitem()
print(a)
print(popped)

# values
view = b.values()
print(view)



'''
From here, see documentation for more details
'''

# Context Manager
# Python’s "with" statement supports the concept of a runtime context defined by a context manager.

# Type Annotation

# Union



# Other Built-in
# The interpreter supports several other kinds of objects.
# Most of these support only one or two operations.

# Modules

# Classes and Clas Instances

# Functions

# Methods

# Type Objects

# The Null Object

# Boolean Values



# Special Attributes
# The implementation adds a few special read-only attributes to several object types, where they are relevant.
# Some of these are not reported by the dir() built-in function.



