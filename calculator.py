#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 19:35:59 2018

@author: sarahkenneally
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:26:11 2018

@author: 99993
"""

def add(first, second):
    return first + second

def divide(first, second):
    if second == 0:
        return 'Cannot divide by Zero'
    return first / second

def exponent(first, second):
    return first ** second

def multiply(first, second):
    return first * second

def subtract(first, second):
    return first - second

def squareRoot(first):
    number_types = (int, float, complex)
    if isinstance(first, number_types):
        return math.sqrt() 
    else:
        raise ValueError

def square(first):
    number_types = (int, float, complex)
    y = first**2
    if isinstance(first, number_types):
        return y
    else:
        raise ValueError

def cube(first):
    number_types = (int, float, complex)
    y = first**3
    if isinstance(first, number_types):
        return y
    else:
        raise ValueError

def sin(first):
    number_types = (int, float, complex)
    result = math.sin(first)
    if isinstance(first, number_types):
        return result
    else:
        raise ValueError

def cos(first):
    number_types = (int, float, complex)
    result = math.cos(first)
    if isinstance(first, number_types):
        return result
    else:
        raise ValueError
        
        
def tan(first):
    number_types = (int, float, complex)
    result = math.tan(first)
    if isinstance(first, number_types):
        return result
    else:
        raise ValueError
