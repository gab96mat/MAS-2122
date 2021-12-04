'''
SOURCE:
https://docs.python.org/3/library/stdtypes.html
'''


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
