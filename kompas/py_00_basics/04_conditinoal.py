# Conditional statement allows for conditional execution of a statement or group of statements based on the value of an expression.
""" this is the structure of conditinal statement.

if expression:
    statement

"""

# ex.1
a = 1
if a > 1:
    print("a is greater than 0")
elif a == 0:
    print("a is zero")
else:
    print("a is negative")


# ex.2 conditional expression (shorter version)
b = 0
m = a if a > b else b
print(m, m==a, m==b)
