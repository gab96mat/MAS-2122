'''
This is a sample code for built-in modules.
I selected frequently used modules in my case.
For more details, see source.

SOURCE:
https://docs.python.org/3/library/index.html
'''


# datetime
# https://docs.python.org/3/library/datetime.html

from datetime import date

print(date.today())



# copy
# https://docs.python.org/3/library/copy.html

from copy import deepcopy

data = [i for i in range(10)]
print(data)
data_copied = deepcopy(data)
data_copied[0] = 10
print(data_copied)
print(data==data_copied)



# math
# https://docs.python.org/3/library/math.html

import math

degree = 180
radians = math.radians(degree)
print(radians)



# random
# https://docs.python.org/3/library/random.html

from random import randint

random_list = [randint(0, 100) for i in range(10)]
print(random_list)



# itertools
# https://docs.python.org/3/library/itertools.html

from itertools import repeat

item_to_repeat = 0
count = 10

repetitive_list = list([i for i in repeat(item_to_repeat, count)])
print(repetitive_list)



# shutil
# https://docs.python.org/3/library/shutil.html
from shutil import copyfile

# os
# https://docs.python.org/3/library/os.html
import os

# get directory
HERE = os.path.dirname(os.path.abspath(__file__))
print(HERE)
DST = os.path.join(HERE, 'data')
print(DST)

# copy test.py from HERE to DST
src = os.path.join(HERE, 'test.py')
dst = os.path.join(DST, 'test_copied.py')
copyfile(src, dst)
print('file \n{} \nis successfully copied to \n{}'.format(src, dst))



# time
# https://docs.python.org/3/library/time.html
from time import time

# get start time
start_t = time()

cnt = 0
steps = 10000000
for i in range(steps):
    cnt += 1

# get end time
end_t = time()

# calc difference
calc_time = end_t - start_t
print('calculation time for {} steps is {} second'.format(steps, calc_time))



# argparse
# https://docs.python.org/3/library/argparse.html



# logging
# https://docs.python.org/3/library/logging.html



# json
# https://docs.python.org/3/library/json.html
# see py_03intermediate\read_and_write_json.py



# sys
# https://docs.python.org/3/library/sys.html
import sys
print(sys.path)



# __main__
# https://docs.python.org/3/library/__main__.html
# see py_03_intermediate\if_name_main.py



# keyward
# https://docs.python.org/3/library/keyword.html
import keyword
print(keyword.kwlist)



# imp
# https://docs.python.org/3/library/imp.html
import imp
imp.reload(math)
# ~= compas_ghpython.utilities.unload_modules('math')
# https://compas.dev/compas/latest/api/generated/compas_ghpython.utilities.unload_modules.html#compas_ghpython.utilities.unload_modules
