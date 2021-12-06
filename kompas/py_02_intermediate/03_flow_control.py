


'''precision_control'''



x = 20.000000
y = 90

print ('\nPoint X=' + str(x) + ' Y=' + str(y))
#place holder
print ('Point X={} Y={}'.format(x, y))
#more feature   ex.format float 2 or 5 decimal numbers
print ('Point X={:.2f} Y={:.5f}'.format(x, y))



'''
flow_control

acknowledgement: 
This code is organized based on the lecture by Gonzalo Casas(casas@arch.ethz.ch)
'''



# an example function
def division(a, b):
    return a / b

# call the function
result = division(15, 3)
print('\n{} / {} = {:.1f}'.format(15, 3, result))

# The code below will cause error
# result = division(15, 0)
# to avoid this error which stop the execution, use exceptions!!!!

# how to make own exeption
class MyOwnError(Exception):
    pass

# how to use built-in exception
def try_division(a, b):
    try:
        return a / b
    # predifine the possible exception beforehand
    except ZeroDivisionError:
        # 1. use custom error
        # raise MyOwnError
        
        # 2. do something to keep execution
        return None

# normal calculation
print('{} / {} = {}'.format(15, 3, try_division(15, 3)))
# flow control
print('{} / {} = {}'.format(15, 0, try_division(15, 0)))



'''raise error'''



# if you simply use raise, the execution stops.
def some_algo(a):
    if len(a) == 0:
        raise ValueError
    else:
        print('\npass')


l = [0]
some_algo(l)
l = []
some_algo(l)
