'''
What is a Variable in Python?
A Python variable is a reserved memory location to store values. In other words,
a variable in a python program gives data to the computer for processing.
Every value in Python has a datatype. Different data types in Python are
Numbers, List, Tuple, Strings, Dictionary, etc. Variables can be declared by
any name or even alphabets like a, aa, abc, etc...
SOURCE: http://www.aees.gov.in/htmldocs/downloads/XI_Class_Content_Computer_Science/8-Handout.pdf
'''

'''These are non-sequence types'''
# ex1. Numbers

#     1-1. Integer
zero_int = int()  # how to declare integer type. This is recognized as zero
one_int = int(1)  # integer 1
negative_int = int(-1)  # for negative integer
unclear_int = 10  # you can declare integer without specifying
# print
print('\n\nThese are the integer')
print('zero_int', zero_int, type(zero_int))
print('one_int', one_int, type(one_int))
print('negative_int', negative_int, type(negative_int))
print('unclear_int', unclear_int, type(unclear_int))

#     1-2. Float
zero_float = float()  # how to declare float type. This is recognized as zero
one_float = float(1)  # float 1
negative_float = float(-1)  # for negative float
unclear_float1 = 10.  # you can declare float without specifying
unclear_float2 = 10.0  # you can declare number of decimals
# print
print('\n\nThese are the float')
print('zero_float', zero_float, type(zero_float))
print('one_float', one_float, type(one_float))
print('negative_float', negative_float, type(negative_float))
print('unclear_float1', unclear_float1, type(unclear_float1))
print('unclear_float2', unclear_float2, type(unclear_float2))

#     1-3. Complex Number
complex_num1 = complex(2+3j)  # how to declare complex type.
complex_num2 = 4+6j  # without clear declearation
# print
print('\n\nThese are the complex')
print('complex_num1', complex_num1, type(complex_num1))
print('complex_num2', complex_num2, type(complex_num2))


# ex2. string
string1 = str()  # how to declare the empty string type
string2 = ""  # how to declare the empty string type
string3 = ''  # how to declare the empty string type
#    escape sequences
#    2-1. why single and double quatation?
string4 = "Ko said 'This is why two different types are necessary'."  # vice versa is also true
#    2-1. special meaning of characters with backslash "\"
string5 = 'This is a\nnew line'
# print
print('\n\nThese are the string')
print('string1', string1, type(string1))
print('string2', string2, type(string2))
print('string3', string3, type(string3))
print('string4', string4, type(string4))
print(string5)

# ex3. boolean
bool1 = bool()  # how to declare a bool. This is recognized as False
bool2 = bool(True)  # how to declare a bool: True.
bool3 = True  # without decleration
bool4 = bool(0)  # with zero
bool5 = bool(1)  # and one
# print
print('\n\nThese are the bool')
print('bool1', bool1, type(bool1))
print('bool2', bool2, type(bool2))
print('bool3', bool3, type(bool3))
print('bool4', bool4, type(bool4))
print('bool5', bool5, type(bool5))

'''These are sequence types'''
# ex.4 List
# A list is an ordered and mutable Python container which can hold elements of different types as well as duplicated elements.
print('\n\nThese are the list')
#     4-1. how to declare an empty list
list_a = []
list_b = list()
print("list_a", list_a, type(list_a))
print("list_b", list_b, type(list_b))
# more on list: https://docs.python.org/3/tutorial/datastructures.html


# ex.5 Tuple
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing.
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
print('\n\nThese are the tuple')
tuple_a = ()
print("tuple_a", tuple_a, type(tuple_a))
tuple_b = (0, 1, 2, 3, "4")
print("tuple_b", tuple_b, type(tuple_b))


# ex.6 Dictionary
print('\n\nThese are the dictionary')
# It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary).
# how to declare empty dictionary
dict_a = {}
print("dict_a", dict_a, type(dict_a))
dict_b = dict()
print("dict_b", dict_b, type(dict_b))

# how to add keys and values to dictionary
dict_a['key1'] = 0
dict_a['key2'] = "one"
dict_a['key3'] = True
dict_a['key4'] = [-1, -2, -3]
dict_a['key5'] = (-1, -2, -3)
print(dict_a)

# how to access keys of dictionary
print(dict_a.keys())

# how to access items with a key
print(dict_a.get('key1'))
print(dict_a['key1'])
