'''
SOURCE:
https://docs.python.org/3/library/functions.html
'''

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



# len()
# Return the length (the number of items) of an object.
# The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

print('\nlen()')
print('len({}) returns {}'.format(list_a, len(list_a)))
print('len({}) returns {}'.format(list_b, len(list_b)))
print('len({}) returns {}'.format(list_c, len(list_c)))
print('len({}) returns {}'.format(list_d, len(list_d)))



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



# set()
# Return a new set object, optionally with elements taken from iterable. set is a built-in class.
# https://docs.python.org/3/library/stdtypes.html#types-set
# if you are curious...
# list vs tuple vs set
# https://towardsdatascience.com/15-examples-to-master-python-lists-vs-sets-vs-tuples-d4ffb291cf07



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
