'''
SOURCE:
https://docs.python.org/3/library/functions.html
'''


# bin()
# Convert an integer number to a binary string prefixed with "0b".
e = 100

print('\nbin()')
print('bin({}) returns {}'.format(a, bin(a)))
print('bin({}) returns {}'.format(e, bin(e)))



# chr()
# Return the string representing a character whose Unicode code point is the integer i.

print('\nchr()')
print('chr({}) returns {}'.format(97, chr(97)))



# str()
# Return a str version of object.

zero = str(0)
print('\nstr(0) returns {} which type is {}'.format(zero, type(zero)))



# format()
# Convert a value to a “formatted” representation, as controlled by format_spec.
# The interpretation of format_spec will depend on the type of the value argument;
# however, there is a standard formatting syntax that is used by most built-in types: https://docs.python.org/3/library/string.html#formatspec

print('\nformat()')
print('format({}, {}) returns {}'.format(8, 'b', format(8, 'b')))
print('...converting 8 in to binary representation')



# bool()
# Return a boolean value, one of True or False.
f = 0

print('\nbool()')
print('bool({}) returns {}'.format(a, bool(a)))
print('bool({}) returns {}'.format(f, bool(f)))
