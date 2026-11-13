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

"""
import math

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b



def logarithm(a, b):
    if a <= 0:
        raise ValueError("The base cannot be negative")
    if a == 1:
        raise ValueError("The base cannot equal 1")
    if b <= 0:
        raise ValueError("The value cannot be negative")

    return math.log(b, a)

def exponent(a, b):
    return a ** b


