'''
This file shows example code for path control.
This will be quite helpful for collaboration through github.
SOURCE:
https://docs.python.org/3/library/os.html
'''

# import 
import os

# get the filepath
filepath = os.path.abspath(__file__)
print('\nthe filepath is \n{}'.format(filepath))

# get the parent folder of the filepath
HERE = os.path.dirname(os.path.abspath(__file__))
print('\nthe path of the parent folder of this file is \n{}'.format(HERE))

# get cwd (current working directory)
my_cwd = os.getcwd()
print('\nthe current working directory is \n{}'.format(my_cwd))

# get the directory of 'data' in 'py_03_intermediate' folder
parent_folder = 'py_02_intermediate'
foldername = 'data'
DIR = os.path.join(HERE, foldername)
print('\nthe folderpath to "{}" in "{}" is \n{}'.format(foldername, parent_folder, DIR))

# get the directory of 'data' in 'py_01_builtin' folder
parent_folder = 'py_01_builtin'
foldername = 'data'
DIR = os.path.join(my_cwd, parent_folder, foldername)
print('\nthe folderpath to "{}" in "{}" is \n{}'.format(foldername, parent_folder, DIR))
