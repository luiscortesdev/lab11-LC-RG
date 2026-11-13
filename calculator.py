import math
def add(a, b):
    u = a + b
    return u

def subtract(a, b):
    return a - b

def mul(a, b):
    u = a * b
    return u

def div(a,b):
    if a == 0:
        raise ZeroDivisionError('division by zero')
    u = b / a
    return u

def logarithm(a, b):
    if a <= 0:
        raise ValueError("The base cannot be negative")
    if a == 1:
        raise ValueError("The base cannot equal 1")
    if b <= 0:
        raise ValueError("The value cannot be negative")

    return math.log(b, a)

def exp(a,b):
    u = a ** b
    return u

def square_root(a):
    if a < 0:
        raise ValueError("Cannot get square root of negative value")

    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)


