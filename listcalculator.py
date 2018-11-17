#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 01:01:00 2018

@author: sarahkenneally
"""

import unittest
import math 
from functools  import  reduce


def add(n):
     return (reduce(lambda x,y: x+y, n))

def subtract(n):
    return(reduce(lambda x,y: x-y, n))

def multiply(n):
    return (reduce(lambda x,y: x*y, n))

def exponent(n):
    return(reduce(lambda x,y: x**y, n))
    
    
def divide(n):
    return (reduce(lambda x,y: x/y, n))

def square_root(n):
    return([x for x in map( math.sqrt, n)])
    
def evens(n): 
    return(list(filter(lambda n : n%2==0, n)))
    
def square(n): 
    return([x for x in map(lambda x: x**2, n)])

def cube(n): 
    return ([x for x in map(lambda x: x**3, n)])

def sin(n): 
    return([x for x in map( math.sin, n)])  
  
def cubegenerator(n):
    for value in n:
        yield value**3
cubegenerator = cube ([3, 88,-4])
for value in cube ([3, 88,-4]):
    print (value) 
    

