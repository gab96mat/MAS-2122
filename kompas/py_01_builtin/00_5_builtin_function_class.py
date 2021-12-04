# getattr()
# Return the value of the named attribute of object. name must be a string.
# If the string is the name of one of the object’s attributes, the result is the value of that attribute.
# For example, getattr(x, 'foobar') is equivalent to x.foobar.

# a class to be taken by the getattr()
class Test():
    attr = 0

print('\ngetattr()')
print('getattr({}, {}) returns {}'.format('Test', 'attr', getattr(Test, 'attr')))


# setattr()
# This is the counterpart of getattr(). The arguments are an object, a string, and an arbitrary value.
# The string may name an existing attribute or a new attribute.
# The function assigns the value to the attribute, provided the object allows it.
# For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.

print('\nsetattr()')
print('setattr({}, {}, {}) returns {}'.format('Test', 'attr', 10, setattr(Test, 'attr_set', 10)))
print('Test object obtain attr_set as an attribute, which is: {}'.format(Test.attr_set))



# hasattr()
# The arguments are an object and a string.
# The result is True if the string is the name of one of the object’s attributes, False if not.

print('\nhasattr()')
print('hasattr({}, {}) returns {}'.format('Test', 'attr', hasattr(Test, 'attr')))
print('hasattr({}, {}) returns {}'.format('Test', 'attr', hasattr(Test, 'non-attr')))



# isinstance()
# Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect, or virtual) subclass thereof.

# create an instance to be called
test = Test()

# create a subclass to be called
class SubTest(Test):
    pass
subtest = SubTest()

print('\nisinstance()')
print('test is an instance of object type: {}'.format(isinstance(test, object)))
print('subtest is an instance of object type: {}'.format(isinstance(subtest, object)))
print('subtest is also an instance of Test object: {}'.format(isinstance(subtest, Test)))



# issubclass()
# Return True if class is a subclass (direct, indirect, or virtual) of classinfo.

print('\nissubclass()')
print('subtest is also a subclass of Test class: {}'.format(issubclass(SubTest, Test)))



# @staticmethod
# Transform a method into a static method.
# A static method can be called either on the class (such as C.f()) or on an instance (such as C().f()).
# Moreover, they can be called as regular functions (such as f()).

# inside a class...
class C:
    @staticmethod
    def class_method(arg1):
        return arg1 * 10

result = C.class_method(10) # on an class
print('\nresult of static method is {}'.format(result))
result = C().class_method(10) # on an instance
print('\nresult of static method is {}'.format(result))

# with regular function...
def regular_f(arg1):
    return arg1 * 10

class D:
    method = staticmethod(regular_f)

result = D.method(10)
print('\nresult of static method is {}'.format(result))
result = D().method(10)
print('\nresult of static method is {}'.format(result))
result = regular_f(10)
print('\nresult of regular method is {}'.format(result))



# @classmethod
# Transform a method into a class method.
# A class method receives the class as an implicit first argument, just like an instance method receives the instance.
# To declare a class method, use this idiom:

class E:
    @classmethod
    def f2(self, arg1):
        return arg1 * 2

result = E.f2(10)
print('\nresult of class method is {}'.format(result))
result = E().f2(10)
print('\nresult of class method is {}'.format(result))
