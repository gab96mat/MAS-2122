'''
SOURCE:
https://docs.python.org/3/library/stdtypes.html
'''


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
    