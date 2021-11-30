'''
what is the import statement in python?
import is calling either module or python file into the code which you are writing now!
'''

# ex.1 import a built-in module of python.
import math
print("\nex1. built-in module")
print(math)
print(type(math))

# ex.2-1 import a module which is located in the same folder as this .py file
import module1
print("\nex2-1. module in the same folder")
print(module1)
print(type(module1))

# ex.2-2 import a module which is located in the src folder (need to set __init__.py)
from src import module2
print("\nex2-2. module in the deeper folder")
print(module2)
print(type(module2))
# call the function in the module2
test = module2.test_function()
print(test)

# ex.2-3 directly import a class which is located in the src folder (need to set __init__.py)
from src import TestClass
print("\nex2-2. module in the deeper folder")
print(TestClass)
print(type(TestClass))

# ex.3 import a module from conda environment
import compas
print("\nex3. cnvironment")
print(compas)
print(type(compas))

'''
once you import a module, its "scope" is only in this python component.
what is "scope"? --->  https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Scope.html
'''
