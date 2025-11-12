#https://github.com/mpaquette1-svg/lab11-MP-MEG.git
# task 1 - MP
# task 2 - MEG

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        a / b

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(a,b) # use math library + raise ValueError

def exp(a, b):
    return a ** b



