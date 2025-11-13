# https://github.com/mpaquette1-svg/lab11-MP-MEG.git
#Partner 1: Matthew Paquette
#Partner 2: Miguel Gutierrez

import math

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a != 0:
        return b / a # raise ZeroDivisionError if a == 0
    else:
        raise ZeroDivisionError


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    else:
        return math.log(a,b)# use math library + raise ValueError

def exp(a, b):
    return a**b

