'''
lambda

SOURCE:
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
'''



# lambda
# Small anonymous functions can be created with the lambda keyword.

value = (lambda x : x + 5)(100)
print(value)



#  used case 1
def make_incrementor(n):
    # returning a function with value set as n
    return lambda x: x + n

#  call it
original = 100
incrementor = make_incrementor(original)
print(incrementor)
print(incrementor(0))
print(incrementor(1))
print(incrementor(2))



# used case 2
import random
length = 3
vec3d_list = [(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)) for k in range(length) for j in range(length) for i in range(length)]

# plain sort
plain_sort = sorted(vec3d_list)
# equivalent
equivalent = sorted(vec3d_list, key=lambda k: [k[0], k[1], k[2]])

# z, y, x sort
zyx_sort = sorted(vec3d_list, key=lambda k: [k[2], k[1], k[0]])

print('\nsorted()')
print('\noriginal list: \n{}'.format(vec3d_list))
print('\nsorted({}) returns: \n{}'.format('vec3d_list', plain_sort))
print('\nsorted({}) returns: \n{}'.format('vec3d_list, key=lambda k: [k[0], k[1], k[2]]', equivalent))
print('\nsorted({}) returns: \n{}'.format('vec3d_list, key=lambda k: [k[2], k[1], k[0]]', zyx_sort))
