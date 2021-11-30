'''
A function is a block of code that only runs when it is called.
'''

# ex.1 empty function
print('\n\nex.1')
# define
def empty_function():
    pass
# call
empty_function() #this does nothing though.


# ex.2 function without argument/return
print('\n\nex.2')
# define
def print_func():
    print("print")
# call
print_func()


# ex.3 function with input arguments
print('\n\nex.3')
# define
def func_with_param(arg1, arg2):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
#call
func_with_param(1, "arg2")


# ex.4 function with return statement
print('\n\nex.4')
# define
def return_func():
    return 0
# call
zero = return_func()
print(zero)


# ex.5 function with input arguments and multiple returns
print('\n\nex.5')
# define
def function(arg1, arg2):
    addition = arg1 + arg2
    subtraction = arg1 - arg2
    division = arg1 / arg2
    multiplication = arg1 * arg2
    return addition, subtraction, division, multiplication
# call
output = function(10, 2)
print(output)


# ex.6 function with default arguments
print('\n\nex.6')
# define
def func_with_default(arg1=10, arg2=2):
    addition = arg1 + arg2
    subtraction = arg1 - arg2
    division = arg1 / arg2
    multiplication = arg1 * arg2
    return addition, subtraction, division, multiplication
# call
output = func_with_default() # not necessary to give argument to function
print(output)
