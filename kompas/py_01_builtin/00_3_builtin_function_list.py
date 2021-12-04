'''
SOURCE:
https://docs.python.org/3/library/functions.html
'''

# list()
# Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types — list, tuple, range.

# create a sample list class
import random
list_class = list([random.randint(0, 10) for i in range(10)])

print('\nlist()')
print('list() returns {}'.format(list_class))



# bultin functions of list class

# append
item_to_append = 10
list_class.append(item_to_append)
print('{} is added at the last index of the list: {}'.format(item_to_append, list_class))

# copy
copied_list = list_class.copy()
print('list_class is copied as {}'.format(copied_list))

# count
item_to_count = 0
count = list_class.count(item_to_count)
print('the count of the {} in the {} is {}'.format(item_to_count, list_class, count))

# extend
list_to_extend = list([random.randint(-10, -1) for i in range(5)])
list_class.extend(list_to_extend)
print('a list, {},  is added at the last index of the list: {}'.format(list_to_extend, list_class))

# index
item_to_search = 0
if item_to_search in list_class:
    ind = list_class.index(item_to_search)
    print('the first index of {} in {} is {}'.format(item_to_search, list_class, ind))
else:
    print('{} is not in the list'.format(item_to_search))

# insert
item_to_insert = 4
index_to_insert = 4
list_class.insert(index_to_insert, item_to_insert)
print('{} is inserted at the {}th index: {}'.format(item_to_insert, index_to_insert, list_class))

# pop
index_to_pop = 3
list_class.pop(index_to_pop)
print('the item at the {}th index is poped: {}'.format(index_to_pop, list_class))

# remove
item_to_remove = 4
list_class.remove(item_to_remove)
print('the item {} is removed: {}'.format(item_to_remove, list_class))

# reverse
list_class.reverse()
print('the list is reversed: {}'.format(list_class))

# sort
list_class.sort()
print('the list is sorted: {}'.format(list_class))

# clear
list_class.clear()
print('the list is cleared: {}'.format(list_class))
