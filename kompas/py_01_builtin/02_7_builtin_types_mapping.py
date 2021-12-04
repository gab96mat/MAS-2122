'''
SOURCE:
https://docs.python.org/3/library/stdtypes.html
'''


# Mapping = dict

# multiple ways of defining a dictionary

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(a == b == c == d == e == f)

# dictionary related methods

# list
# Return a list of all the keys used in the dictionary d.
print(list(d))

# len
# Return the number of items in the dictionary d.
print(len(d))

# d[key]
# Return the item of d with key key. Raises a KeyError if key is not in the map.
print(d['one'])

# d[key] = value
# Set d[key] to value.
d['one'] = 1.0
print(d['one'])

# del d[key]
# Remove d[key] from d. Raises a KeyError if key is not in the map.
del d['one']
print(d)

# key in d
# Return True if d has a key key, else False.
key_to_check = 'four'
print(key_to_check in d)

# key not in d
# Equivalent to not key in d.
print(key_to_check not in d)

# iter
# Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys()).
iterator = iter(d)
print(iterator)
print(iterator.__next__())
print(iterator.__next__())
# print(iterator.__next__()) this will be out of range

# clear()
# Remove all items from the dictionary.
d.clear()
print(d)

# copy
# Return a shallow copy of the dictionary.
a_copied = a.copy()
print(a_copied)

# get
# Return the value for key if key is in the dictionary, else default.
# If default is not given, it defaults to None, so that this method never raises a KeyError.
value_to_get = a.get('one')
print(value_to_get)

# items
# Return a new view of the dictionary’s items ((key, value) pairs).
view = a.items()
print(view)

# keys
# Return a new view of the dictionary’s keys
view = a.keys()
print(view)

# pop
# If key is in the dictionary, remove it and return its value, else return default.
# If default is not given and key is not in the dictionary, a KeyError is raised.
a.pop('one')
print(a)

# popitem
popped = a.popitem()
print(a)
print(popped)

# values
view = b.values()
print(view)
