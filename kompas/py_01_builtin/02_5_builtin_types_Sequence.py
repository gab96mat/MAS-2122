# Sequence
# There are three basic sequence types: lists, tuples, and range objects.
# Additional sequence types tailored for processing of binary data and text strings are described in dedicated sections.

sequence_list = list([i for i in range(10)])
sequence_tuple = tuple((i for i in range(10)))
sequence_range = range(10)

print('\nSequence')
print('list: {}'.format(sequence_list))
print('tuple: {}'.format(sequence_tuple))
print('range: {}'.format(sequence_range))

# operations

item_to_check = -1

# in
if item_to_check in sequence_list:
    print('{} is in the list'.format(item_to_check))
else:
    print('{} is NOT in the list'.format(item_to_check))

# not in
if item_to_check not in sequence_list:
    print('{} is NOT in the list'.format(item_to_check))
else:
    print('{} is in the list'.format(item_to_check))

# +
list_a = list([i for i in range(10)])
list_b = list([i*10 for i in range(10)])
concatenated = list_a + list_b
print('concatenated list is {}'.format(concatenated))

# *
multiplied = list_a * 2
print('multiplied is {}'.format(multiplied))

# slicing
index = 0
item_at_index = list_a[index]
print('{}th index in the {} is {}'.format(index, list_a, item_at_index))

start_ind = 2
end_ind = 6
sliced_list = list_a[start_ind:end_ind]
print('{} is extracted from {}th to {}th index of the {}'.format(sliced_list, start_ind, end_ind-1, list_a))

step = 2
sliced_list = list_a[start_ind:end_ind:step]
print('{} is every {}th items from {}th to {}th index of the {}'.format(sliced_list, step, start_ind, end_ind-1, list_a))

# muting
replacement = 100
index_to_replace = 3
list_a[index_to_replace] = replacement
print(list_a)

replacement = list([i*100 for i in range(1, 4)])
start_index_to_replace = 3
end_index_to_replace = 6
list_a[start_index_to_replace:end_index_to_replace] = replacement
print(list_a)

start_index_to_delete = 3
end_index_to_delete = 6
del list_a[start_index_to_delete:end_index_to_delete]
print(list_a)

times_to_repeat = 3
list_a *= times_to_repeat
print(list_a)
