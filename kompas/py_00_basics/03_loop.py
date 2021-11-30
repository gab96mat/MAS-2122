# ex.1 for loop
print('\n\nThese are the for loop')
for i in range(3):
    print(i) # start with zero

# ex.2 while loop
print('\n\nThese are the while loop')
count = 0
while count < 3:
    print(count)
    count = count + 1
    # count += 1

# ex.3 nested loop
print('\n\nThese are the nested loop')
for i in range(3): # first loop
    for j in range(3): # second loop
        for k in range(3): # third loop
            print("i:", i, "j:", j, "k:", k)

# ex.4 loop control statement(break, continue, pass)
#    4-1. break
print('\n\nThese are the break')
#        breaks out of the innermost enclosing for or while loop.
count = 0
container = []
import random as r
while count < 100:
    count += 1
    factor = r.random()
    container.append(factor)
    if factor > 0.8:
        print("factor was greater than 0.8 at iteration {}".format(len(container)))
        break

#    4-2. continue
#        continues with the next iteration of the loop
print('\n\nThese are the continue')
for num in range(3):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

#    4-3. pass
print('\n\nThese are the pass')
#        The pass statement does nothing
for i in range(3):
    pass
# can be used for a place-holder for function or class
def nothing():
    pass


# ex.5 list comprehension
print('\n\nThese are the list comprehension')
#    List comprehensions are a second way of making lists in shorter line.
comprehension = [i for i in range(10)]
print("comprehension", comprehension, type(comprehension))
"""same to
comprehension = []
for i in range(10):
    comprehension.append(i)
"""

comprehension_if = [i  if i%2==0 else "odd" for i in range(10)]
print("comprehension_if", comprehension_if, type(comprehension_if))
"""same to
comprehension_if = []
for i in range(10):
    if i % 2 == 0:
        comprehension_if.append(i)
    else:
        comprehension_if.append("odd")
"""
