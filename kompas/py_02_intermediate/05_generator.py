'''
generator

acknowledgement: 
This code is organized based on the lecture by Gonzalo Casas(casas@arch.ethz.ch)
'''


# a function intended to be infintie
# to avoid this, there are several ways...

# 1. use if statement
def factorial(n):
    if n ==1:
        return n
    else:
        return n * factorial(n-1)

iteration = 5
print('\nthe {}th iteration of fractorial is {}\n'.format(iteration, factorial(iteration)))



# 2-1. create generator with yield
def all_factorials():
    n = 0
    # this keep statement always true
    while True:
        n +=1
        # with yield, syntax remenber what it was and pick up it
        yield factorial(n)

# 2-2. Query an generator
for i in all_factorials():
    print(i)
    if i > 1000:
        break



# what is generator btw...?
a_sequence_of_all_factorials = all_factorials()
print('\nthis is a generator\n{}'.format(a_sequence_of_all_factorials))

# how to access generated values one by one
print(next(a_sequence_of_all_factorials))
print(next(a_sequence_of_all_factorials))
print(next(a_sequence_of_all_factorials))
print(next(a_sequence_of_all_factorials))

# you already know some of the generator-like object
# precisely speaking, this is not generator though...
# https://stackoverflow.com/questions/23663231/does-enumerate-produce-a-generator-object
sample = [i for i in range(10)]
enumerator = enumerate(sample)
print(enumerator)
print(next(enumerator))
print(next(enumerator))
print(next(enumerator))
print(next(enumerator))
