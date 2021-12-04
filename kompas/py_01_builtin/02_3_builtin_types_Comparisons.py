'''
SOURCE:
https://docs.python.org/3/library/stdtypes.html
'''


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

