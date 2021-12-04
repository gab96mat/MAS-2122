

# help()
print('\nhelp()')
# print(help())



# input()
# If the prompt argument is present, it is written to standard output without a trailing newline.
# The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that.

uset_input_value = None # input('type whatever you like and press enter: \n')
print('\ninput()')
print('input() takes user input in the terminal and returns "{}"'.format(uset_input_value))



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



# print()
# Print objects to the text stream file, separated by sep and followed by end.
# sep, end, file, and flush, if present, must be given as keyword arguments.

print('\nthis is a plain print')
print(list_a, list_b, list_c)
print('\nthis is print with extra arguments')
print(list_a, list_b, list_c, sep='\n', end='\n...fin\n')



# callable()
# Return True if the object argument appears callable, False if not.
# If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed. 

import math
print('\ncallable()')
print('callable({}) returns {}'.format(a, callable(a)))
print('callable({}) returns {}'.format('math.radians', callable(math.radians)))



# dir()
# Without arguments, return the list of names in the current local scope.
# With an argument, attempt to return a list of valid attributes for that object.

print('\ndir()')
print('dir() returns {}'.format(dir()))
print('dir(math) returns {}'.format(dir(math)))



# globals()
# Return a dictionary representing the current global symbol table.

print('\nglobals()')
print('globals() returns {}'.format(globals()))



# locals()
# Update and return a dictionary representing the current local symbol table.
# Note that at the module level, locals() and globals() are the same dictionary.

print('\nlocals()')
print('locals() returns {}'.format(locals()))



# vars()
# Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute

import math
print('\nvars()')
print('vars(math) returns {}'.format(vars(math)))



# type()
# With one argument, return the type of an object.
# The return value is a type object and generally the same object as returned by object.__class__

print('\ntype()')
print('the type of {} is {}'.format(0, type(0)))
print('the type of {} is {}'.format(0, type('a')))
print('the type of {} is {}'.format(0, type(0.1)))
print('the type of {} is {}'.format(0, type(True)))
print('the type of {} is {}'.format(0, type(regular_f)))