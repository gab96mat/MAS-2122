'''
This file contains most of the function in the source website.
For more classified version, see 00_NUM_builtin_function_TOPIC.py

SOURCE:
https://docs.python.org/3/library/functions.html
'''


# abs()
# Return the absolute value of a number
a = 1
b = -1
c = 0.01
d = -0.01

print('\nabs()')
print('abs({}) returns {}'.format(a, abs(a)))
print('abs({}) returns {}'.format(b, abs(b)))
print('abs({}) returns {}'.format(c, abs(c)))
print('abs({}) returns {}'.format(d, abs(d)))



# all()
# Return True if all elements of the iterable are true.
list_a = [True, True, True]
list_b = [False, True, True]

print('\nall()')
print('all({}) returns {}'.format(list_a, all(list_a)))
print('all({}) returns {}'.format(list_b, all(list_b)))



# any()
# Return True if any element of the iterable is true.
# If the iterable is empty, return False.
list_c = [False, False, False]

print('\nany()')
print('any({}) returns {}'.format(list_a, any(list_a)))
print('any({}) returns {}'.format(list_b, any(list_b)))
print('any({}) returns {}'.format(list_c, any(list_c)))



# bin()
# Convert an integer number to a binary string prefixed with "0b".
e = 100

print('\nbin()')
print('bin({}) returns {}'.format(a, bin(a)))
print('bin({}) returns {}'.format(e, bin(e)))



# bool()
# Return a boolean value, one of True or False.
f = 0

print('\nbool()')
print('bool({}) returns {}'.format(a, bool(a)))
print('bool({}) returns {}'.format(f, bool(f)))



# callable()
# Return True if the object argument appears callable, False if not.
# If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed. 

import math
print('\ncallable()')
print('callable({}) returns {}'.format(a, callable(a)))
print('callable({}) returns {}'.format('math.radians', callable(math.radians)))



# chr()
# Return the string representing a character whose Unicode code point is the integer i.

print('\nchr()')
print('chr({}) returns {}'.format(97, chr(97)))



# dir()
# Without arguments, return the list of names in the current local scope.
# With an argument, attempt to return a list of valid attributes for that object.

print('\ndir()')
print('dir() returns {}'.format(dir()))
print('dir(math) returns {}'.format(dir(math)))



# divmod()
# Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.

print('\ndivmod()')
print('divmod({}, {}) returns {}'.format(13, 2, divmod(13, 2)))
print('divmod({}, {}) returns {}'.format(2.3, 2, divmod(1.3, 2)))



# enumerate()
# Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.

print('\nenumerate()')
print('enumerate({}) returns {}'.format(list_b, enumerate(list_b, start=0)))

# equivalent to...
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

# how to access the tuple from enumerate object
enu = enumerate(list_b)
print('1st value: {}'.format(enu.__next__()))
print('2nd value: {}'.format(enu.__next__()))
print('3rd value: {}'.format(enu.__next__()))
# print(enu.__next__()) This is out of range

# normally used like...
for index, item in enumerate(list_b, start=0):
    print('index: {}, item: {}'.format(index, item))



# filter()
# Construct an iterator from those elements of iterable for which function returns true.
# Iterable may be either a sequence, a container which supports iteration, or an iterator.
# If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.

# function to be used in filter()
def check_negative(value):
    if value < 0:
        return True
    else:
        return False

# list to be used in filter()
list_d = [-3, -2, -1, 0, 1, 2, 3]

print('\nfilter()')
print('filter({}, {}) returns {}'.format('check_negative', list_d, filter(check_negative, list_d)))

# how to access the tuple from enumerate object
filter_obj = filter(check_negative, list_d)
print('1st value: {}'.format(filter_obj.__next__()))
print('2nd value: {}'.format(filter_obj.__next__()))
print('3rd value: {}'.format(filter_obj.__next__()))
# print(filter_obj.__next__()) This is out of range

# normally used like...
for item in filter(check_negative, list_d):
    print('filtered item: {}'.format(item))



# format()
# Convert a value to a “formatted” representation, as controlled by format_spec.
# The interpretation of format_spec will depend on the type of the value argument;
# however, there is a standard formatting syntax that is used by most built-in types: https://docs.python.org/3/library/string.html#formatspec

print('\nformat()')
print('format({}, {}) returns {}'.format(8, 'b', format(8, 'b')))
print('...converting 8 in to binary representation')



# getattr()
# Return the value of the named attribute of object. name must be a string.
# If the string is the name of one of the object’s attributes, the result is the value of that attribute.
# For example, getattr(x, 'foobar') is equivalent to x.foobar.

# a class to be taken by the getattr()
class Test():
    attr = 0

print('\ngetattr()')
print('getattr({}, {}) returns {}'.format('Test', 'attr', getattr(Test, 'attr')))



# globals()
# Return a dictionary representing the current global symbol table.

print('\nglobals()')
print('globals() returns {}'.format(globals()))



# hasattr()
# The arguments are an object and a string.
# The result is True if the string is the name of one of the object’s attributes, False if not.

print('\nhasattr()')
print('hasattr({}, {}) returns {}'.format('Test', 'attr', hasattr(Test, 'attr')))
print('hasattr({}, {}) returns {}'.format('Test', 'attr', hasattr(Test, 'non-attr')))


# help()
print('\nhelp()')
# print(help())



# input()
# If the prompt argument is present, it is written to standard output without a trailing newline.
# The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that.

uset_input_value = None # input('type whatever you like and press enter: \n')
print('\ninput()')
print('input() takes user input in the terminal and returns "{}"'.format(uset_input_value))



# int()
# Return an integer object constructed from a number or string x, or return 0 if no arguments are given.

print('\nint()')
print('int({}) returns {}'.format(a, int(a)))
print('int({}) returns {}'.format(b, int(b)))
print('int({}) returns {}'.format(c, int(c)))
print('int({}) returns {}'.format(d, int(d)))



# isinstance()
# Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect, or virtual) subclass thereof.

# create an instance to be called
test = Test()

# create a subclass to be called
class SubTest(Test):
    pass
subtest = SubTest()

print('\nisinstance()')
print('test is an instance of object type: {}'.format(isinstance(test, object)))
print('subtest is an instance of object type: {}'.format(isinstance(subtest, object)))
print('subtest is also an instance of Test object: {}'.format(isinstance(subtest, Test)))



# issubclass()
# Return True if class is a subclass (direct, indirect, or virtual) of classinfo.

print('\nissubclass()')
print('subtest is also a subclass of Test class: {}'.format(issubclass(SubTest, Test)))



# iter()



# len()
# Return the length (the number of items) of an object.
# The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

print('\nlen()')
print('len({}) returns {}'.format(list_a, len(list_a)))
print('len({}) returns {}'.format(list_b, len(list_b)))
print('len({}) returns {}'.format(list_c, len(list_c)))
print('len({}) returns {}'.format(list_d, len(list_d)))



# list()
# Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types — list, tuple, range.

print('\nlist()')
print('list() returns {}'.format(list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))



# locals()
# Update and return a dictionary representing the current local symbol table.
# Note that at the module level, locals() and globals() are the same dictionary.

print('\nlocals()')
print('locals() returns {}'.format(locals()))



# map()
# filter()
# Construct an iterator from those elements of iterable for which function returns true.
# Iterable may be either a sequence, a container which supports iteration, or an iterator.
# If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.

# function to be used in map()
def multiply(value):
    return value * (-1)

# list to be used in map()
list_e = [-1, 0, 1]

print('\nmap()')
print('map({}, {}) returns {}'.format('multiply', list_d, map(multiply, list_e)))

# how to access the tuple from enumerate object
mapped_obj = map(multiply, list_e)
print('1st value: {}'.format(mapped_obj.__next__()))
print('2nd value: {}'.format(mapped_obj.__next__()))
print('3rd value: {}'.format(mapped_obj.__next__()))
# print('3rd value: {}'.format(mapped_obj.__next__())) This will be out of range...

# normally used like...
for item in map(multiply, list_d):
    print('mapped item: {}'.format(item))



# max()
# Return the largest item in an iterable or the largest of two or more arguments.

print('\nmax()')
print('max({}) returns {}'.format('list_e', max(list_e)))
print('max({}) returns {}'.format('1, 2, 3', max(1, 2, 3)))



# min()
# Return the smallest item in an iterable or the smallest of two or more arguments.

print('\nmin()')
print('min({}) returns {}'.format('list_e', min(list_e)))
print('min({}) returns {}'.format('1, 2, 3', min(1, 2, 3)))



# next()
# Retrieve the next item from the iterator by calling its __next__() method.

def generator():
    for i in range(5):
        yield i

gen = generator()

print('\nnext()')
print('1st next({}) returns {}'.format('gen', next(gen)))
print('2nd next({}) returns {}'.format('gen', next(gen)))
print('3rd next({}) returns {}'.format('gen', next(gen)))
print('4th next({}) returns {}'.format('gen', next(gen)))
# print(next(gen)) This is out of range



# open()
# Open file and return a corresponding file object.
# If the file cannot be opened, an OSError is raised.
# --------> see py_03_intermediate how_to_read_and_write_json.py

# get filepath to open
import os
HERE = os.path.dirname(__file__)
DIR = os.path.join(HERE, 'data')
FILEPATH = os.path.join(DIR, 'test_file.txt')
print('\n{}'.format(FILEPATH))

# open the file
file_obj = open(FILEPATH, mode='r')
contents = file_obj.read()

print('\nopen()')
print('open({}) returns {}'.format('FILEPATH, mode="r"', file_obj))
print('the contents of the file_obj is {}'.format(contents))

# close the file
file_obj.close()



# pow()
# Return base to the power exp; if mod is present, return base to the power exp, modulo mod (computed more efficiently than pow(base, exp) % mod).
# The two-argument form pow(base, exp) is equivalent to using the power operator: base**exp.

base = 2
exp = 3

powered = pow(base, exp)

print('\npow()')
print('pow({}, {}) returns {}'.format(base, exp, powered))
print('pow({}, {}) and {}**{} are same: {}'.format(base, exp, base, exp, powered == base**exp))



# print()
# Print objects to the text stream file, separated by sep and followed by end.
# sep, end, file, and flush, if present, must be given as keyword arguments.

print('\nthis is a plain print')
print(list_a, list_b, list_c)
print('\nthis is print with extra arguments')
print(list_a, list_b, list_c, sep='\n', end='\n...fin\n')



# range()
# Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence Types — list, tuple, range.

# plain
temp1 = []
for i in range(10):
    temp1.append(i)

# equivalent
temp2 = []
for i in range(0, 10, 1):
    temp2.append(i)

# customized
temp3 = []
start = 0
stop = 10
step = 2
for i in range(start, stop, step):
    temp3.append(i)

print('\nrange()')
print('plain: {}'.format(temp1))
print('equivalent: {}'.format(temp2))
print('customized: {}'.format(temp3))



# reversed()
# Return a reverse iterator.
reversed_gen = reversed(list_e)
list_f = [i for i in range(5)]

# plain
temp1 = []
for i in list_f:
    temp1.append(i)

# reversed
temp2 = []
for i in reversed(list_f):
    temp2.append(i)

# equivalent
temp3 = []
for i in range(len(list_f), 0, -1):
    temp3.append(i)

print('\nreversed()')
print('reversed({}) returns {}'.format(list_f, reversed_gen))
print('plain: {}'.format(temp1))
print('reversed: {}'.format(temp2))
print('equivalent: {}'.format(temp3))



# round()
# Return number rounded to ndigits precision after the decimal point.
# If ndigits is omitted or is None, it returns the nearest integer to its input.

a_float = 123.456
a_rounded = round(a_float)

floats = [i * 0.1 for i in range(11)]
rounds = [round(i * 0.1) for i in range(11)]

print('\nround()')
print('round({}) returns {}'.format(a_float, a_rounded))
print('floats: {}'.format(floats))
print('rounds: {}'.format(rounds))



# set()
# Return a new set object, optionally with elements taken from iterable. set is a built-in class.
# https://docs.python.org/3/library/stdtypes.html#types-set
# if you are curious...
# list vs tuple vs set
# https://towardsdatascience.com/15-examples-to-master-python-lists-vs-sets-vs-tuples-d4ffb291cf07



# setattr()
# This is the counterpart of getattr(). The arguments are an object, a string, and an arbitrary value.
# The string may name an existing attribute or a new attribute.
# The function assigns the value to the attribute, provided the object allows it.
# For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.

print('\nsetattr()')
print('setattr({}, {}, {}) returns {}'.format('Test', 'attr', 10, setattr(Test, 'attr_set', 10)))
print('Test object obtain attr_set as an attribute, which is: {}'.format(Test.attr_set))



# sorted()
# Return a new sorted list from the items in iterable.

import random
length = 3
vec3d_list = [(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)) for k in range(length) for j in range(length) for i in range(length)]

# plain sort
plain_sort = sorted(vec3d_list)
# equivalent
equivalent = sorted(vec3d_list, key=lambda k: [k[0], k[1], k[2]])

# z, y, x sort
zyx_sort = sorted(vec3d_list, key=lambda k: [k[2], k[1], k[0]])

print('\nsorted()')
print('\noriginal list: \n{}'.format(vec3d_list))
print('\nsorted({}) returns: \n{}'.format('vec3d_list', plain_sort))
print('\nsorted({}) returns: \n{}'.format('vec3d_list, key=lambda k: [k[0], k[1], k[2]]', equivalent))
print('\nsorted({}) returns: \n{}'.format('vec3d_list, key=lambda k: [k[2], k[1], k[0]]', zyx_sort))



# @staticmethod
# Transform a method into a static method.
# A static method can be called either on the class (such as C.f()) or on an instance (such as C().f()).
# Moreover, they can be called as regular functions (such as f()).

# inside a class...
class C:
    @staticmethod
    def class_method(arg1):
        return arg1 * 10

result = C.class_method(10) # on an class
print('\nresult of static method is {}'.format(result))
result = C().class_method(10) # on an instance
print('\nresult of static method is {}'.format(result))

# with regular function...
def regular_f(arg1):
    return arg1 * 10

class D:
    method = staticmethod(regular_f)

result = D.method(10)
print('\nresult of static method is {}'.format(result))
result = D().method(10)
print('\nresult of static method is {}'.format(result))
result = regular_f(10)
print('\nresult of regular method is {}'.format(result))



# @classmethod
# Transform a method into a class method.
# A class method receives the class as an implicit first argument, just like an instance method receives the instance.
# To declare a class method, use this idiom:

class E:
    @classmethod
    def f2(self, arg1):
        return arg1 * 2

result = E.f2(10)
print('\nresult of class method is {}'.format(result))
result = E().f2(10)
print('\nresult of class method is {}'.format(result))



# str()
# Return a str version of object.

zero = str(0)
print('\nstr(0) returns {} which type is {}'.format(zero, type(zero)))



# sum()
# Sums start and the items of an iterable from left to right and returns the total.
# The iterable’s items are normally numbers, and the start value is not allowed to be a string.

summed = sum(list_f)
print('\nsum()')
print('sum of {} is {}'.format(list_f, summed))



# type()
# With one argument, return the type of an object.
# The return value is a type object and generally the same object as returned by object.__class__

print('\ntype()')
print('the type of {} is {}'.format(0, type(0)))
print('the type of {} is {}'.format(0, type('a')))
print('the type of {} is {}'.format(0, type(0.1)))
print('the type of {} is {}'.format(0, type(True)))
print('the type of {} is {}'.format(0, type(regular_f)))



# vars()
# Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute

import math
print('\nvars()')
print('vars(math) returns {}'.format(vars(math)))



# zip()
# Iterate over several iterables in parallel, producing tuples with an item from each one.
# More formally: zip() returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument iterables.

list_g = [i for i in range(10)]
list_h = [i*0.1 for i in range(8)]

print('\nzip()')
# normally...
for g, h in zip(list_g, list_h):
    print(g,h)

# formally...
zip_obj = zip(list_g, list_h)
print('\nzip_obj')
print('1st item of zip obj is {}'.format(zip_obj.__next__()))
print('2nd item of zip obj is {}'.format(zip_obj.__next__()))
print('3rd item of zip obj is {}'.format(zip_obj.__next__()))
print('4th item of zip obj is {}'.format(zip_obj.__next__()))
print('5th item of zip obj is {}'.format(zip_obj.__next__()))
