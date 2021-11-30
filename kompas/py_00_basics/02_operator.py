'''
what is the operator in python?
operators are special symbols that designate that some sort of computation should be performed.
'''

# ex.1 Arithmetic operator.
a = +2  # Unary positive
b = -3  # Unary negation
print(a, b)
print("Addition", a + b)
print("Subtraction", a - b)
print("Division", a / b)
print("Modulo", b % a)
print("Floor division", a // b)
print("Multiplication", a * b)
print("Exponentiation", b ** a)

# ex.2 Comparison operator.
print("Equal to", a == b)
print("Not equal to", a != b)
print("Less than", a < b)
print("Less than or equal to", a <= b)
print("Greater than", a > b)
print("Greater than or equal to", a >= b)

# ex.3 Logical operator.
if a is not 0:
    print("This is a not operator")

if (a > 0) or (b > 0):
    print("This is a or operator")

if (a > 0) and (b < 0):
    print("This is an and operator")
