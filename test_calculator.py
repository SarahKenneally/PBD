#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 19:39:10 2018

@author: sarahkenneally
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:39:17 2018

@author: 99993
"""

import unittest
import math 

from calculator import add, divide, exponent, multiply, subtract, squareRoot, square, cube, sin

class CalculatorTest(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(4, add(2, 2))
        self.assertEqual(5, add(2, 3))
        self.assertEqual(5, add(5, 0))
        self.assertEqual(1, add(2, -1))

    def testDivide(self):
        self.assertEqual(1, divide(2, 2))
        self.assertEqual(4, divide(2, 0.5))
        self.assertEqual(5, divide(5, 1))
        self.assertEqual('Cannot divide by Zero', divide(5, 0))

    def testExponent(self):
        self.assertEqual(32, exponent(2, 5))
        self.assertEqual(2, exponent(2, 1))
        self.assertEqual(2, exponent(4, 0.5))
        self.assertEqual(1, exponent(2, 0))

    def testMultiply(self):
        self.assertEqual(4, multiply(2, 2))
        self.assertEqual(0, multiply(5, 0))
        self.assertEqual(5, multiply(5, 1))

    def testSubtract(self):
        self.assertEqual(0, subtract(2, 2))
        self.assertEqual(5, subtract(5, 0))
        self.assertEqual(-1, subtract(2, 3))


    def testSquareRoot(self):
        self.assertEqual(10, math.sqrt(100))
        self.assertEqual(3, math.sqrt(9))
        self.assertEqual(5.744562646538029, math.sqrt(33))
        
    def testSquare(self):
        self.assertEqual(4, square(2))
        self.assertEqual(25, square(5)) 
        self.assertEqual(9, square(-3))
        
    def testCube(self):
        self.assertEqual(681472, cube(88))
        self.assertEqual(-64, cube(-4)) 
        self.assertEqual(93576.66399999999, cube(45.4)) 
        
    def testSin(self):
        self.assertEqual(0.8939966636005579, math.sin(90))
        self.assertEqual(-0.8414709848078965, math.sin(-1))
        self.assertEqual(-0.44964746453460147, math.sin(12.1))
    
    def testCos(self):
        self.assertEqual(0.9649660284921133, math.cos(50))
        self.assertEqual(0.2836621854632263, math.cos(-5))
        self.assertEqual(0.0707372016677029,math.cos(1.5))
        
        
unittest.main()
