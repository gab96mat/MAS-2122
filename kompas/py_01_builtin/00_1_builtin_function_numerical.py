'''
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



# divmod()
# Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.

print('\ndivmod()')
print('divmod({}, {}) returns {}'.format(13, 2, divmod(13, 2)))
print('divmod({}, {}) returns {}'.format(2.3, 2, divmod(1.3, 2)))



# int()
# Return an integer object constructed from a number or string x, or return 0 if no arguments are given.

print('\nint()')
print('int({}) returns {}'.format(a, int(a)))
print('int({}) returns {}'.format(b, int(b)))
print('int({}) returns {}'.format(c, int(c)))
print('int({}) returns {}'.format(d, int(d)))



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



# pow()
# Return base to the power exp; if mod is present, return base to the power exp, modulo mod (computed more efficiently than pow(base, exp) % mod).
# The two-argument form pow(base, exp) is equivalent to using the power operator: base**exp.

base = 2
exp = 3

powered = pow(base, exp)

print('\npow()')
print('pow({}, {}) returns {}'.format(base, exp, powered))
print('pow({}, {}) and {}**{} are same: {}'.format(base, exp, base, exp, powered == base**exp))



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



# sum()
# Sums start and the items of an iterable from left to right and returns the total.
# The iterable’s items are normally numbers, and the start value is not allowed to be a string.

summed = sum(list_f)
print('\nsum()')
print('sum of {} is {}'.format(list_f, summed))
