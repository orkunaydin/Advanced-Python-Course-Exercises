"""Docstring for the simple_math module.

This module includes many simple mathematical functions such as<
addition, substraction, multiplication and division. Additionally,
polynamials of first and second orders can be computed using
functions written in the module.

"""

def simple_add(a,b):
    return a+b

def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)
