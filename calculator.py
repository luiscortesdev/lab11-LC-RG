
import math
def add(a, b):
    u = a + b
    return u

def sub(a, b):
    u = a - b
    return u

def mul(a, b):
    u = a * b
    return u

def div(a,b):
    if a == 0:
        raise ZeroDivisionError('division by zero')
    u = b / a
    return u

def log (a,b):
    if a < 0:
        raise ValueError("Cannot be negative")
    elif a == 0:
        raise ValueError("Cannot be zero")
    if b < 0:
        raise ValueError("Cannot be negative")
    elif b == 0:
        raise ValueError("Cannot be zero")
    u = math.log(a,b)
    return u

def exp (a,b):
    u = a ** b
    return u

