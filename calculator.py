"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot get square root of negative value")

    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0")

    return b / a

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

