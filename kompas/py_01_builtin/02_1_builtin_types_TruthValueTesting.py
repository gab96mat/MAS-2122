'''
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
