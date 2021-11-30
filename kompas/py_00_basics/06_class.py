'''
a class is an extensible program-code-template
for creating objects, providing initial values
for state (member variables)
and implementations of behavior (member functions or methods)
SOURCE: https://en.wikipedia.org/wiki/Class_(computer_programming)

simply speaking,
class normally has attributes and method,
which is defined by user.
'''


# ex.1 simple class structure
class Beginner(object):
    pass

b = Beginner()
print("b", b, type(b))


# ex.2 simple class with attributes and methods (or property and function)
class Elementary(object):

    # this is a class variable
    attr0 = "class variable"

    # initiate function which will automatically run and initiate object when the class is called.
    def __init__(self, argument):
        # these are instance variable
        self.attr1 = "hardcoded"
        self.attr2 = argument

        # this is an attribute defined by internal method
        self.attr5 = self.method5(argument)

    # this is a method which will run only if it's called.
    def method0(self):
        print("you call the method0")

    # this is a method with input argument.
    def method1(self, argument1):
        print("this is the method1. the argument is ", argument1)

    # this is a method with input argument and return.
    def method2(self, argument2):
        result = argument2 * 10
        print("this is the method2. the argument is {}, the result is {}".format(argument2, result))
        return result

    # this is a method with input argument which will create a new attribute
    def method3(self, argument3):
        self.attr3 = argument3

    # this is a method with input argument which will create a new attribute and return
    def method4(self, argument4):
        self.attr4 = argument4
        return self.attr4

    # this is a method which will be called in the __init__ funtion.
    def method5(self, argument):
        characters = []
        for c in argument:
            characters.append(c)
        return characters


# call object
e = Elementary(argument="argument") # at this moment, __init__ function is already called.
print("e", e, type(e))

# call attributes
print("attr0", e.attr0, type(e.attr0))
print("attr1", e.attr1, type(e.attr1))
print("attr2", e.attr2, type(e.attr2))

# call method0
e.method0()

# call method1
e.method1(1)

# call method2 and assign returned value into variable(=result)
var2 = e.method2(2)
print(var2)

# call method3
e.method3(3)
# call updated attribute by method3
print("attr3", e.attr3)

# call method4
var4 = e.method4(4)
# call updated attribute by method4
print("attr4", e.attr4)
print("var4", var4)

# call attr5
print("attr5", e.attr5, type(e.attr5))
