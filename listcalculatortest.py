#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 02:43:21 2018

@author: sarahkenneally
"""

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
from functools  import  reduce


from listcalculator import add, subtract, multiply, exponent, divide, square_root, square,cube, sin, evens, cubegenerator

class CalculatorTest(unittest.TestCase):
    
    
    def testAdd(self):
        self.assertEqual(6, add([1,2,3]))
        self.assertEqual(-7, add([-1,-3,-3]))
        self.assertEqual(12, add([10,-3,5]))
    
    def testSubtract(self):
        self.assertEqual(-5, subtract([1,3,3]))
        self.assertEqual(5, subtract([-1,-3,-3]))
        self.assertEqual(-17, subtract([10,30,-3]))
        
    def testMultiply(self):
        self.assertEqual(9, multiply([1,3,3]))
        self.assertEqual(100, multiply([5,5,4]))
       
    def testExponent(self):
        self.assertEqual(32, exponent([2, 5,1]))
        self.assertEqual(729, exponent([3,3,2]))
        self.assertEqual(79766443076872509863361, exponent([3,6,2,4]))
    
    
    def testDivide(self):
        self.assertEqual(25, divide([200,2,4]))
        self.assertEqual(-5, divide([25,-5,1]))
        self.assertEqual(-25, divide([-200,-2,-4]))
        #self.assertEqual('Cannot divide by Zero', divide([6,2,0]))
        
    
    def testSquareRoot(self):
        self.assertEqual([10,3,1.452583904633395],square_root ([100,9, 2.11]))
        self.assertEqual([5.744562646538029,5,0], square_root([33,25, 0]))
    
    
    def testSquare(self):
        self.assertEqual([49,100,3136, 6.25],square ([7,10,56, 2.5]))
        self.assertEqual([4,25,9],square ([-2,-5,-3]))
    
    def testCube(self):
        self.assertEqual([343,1000,1728, 24.389],cube ([7,10,12, 2.9]))
        self.assertEqual([-64, -343, -1000, -1728],cube ([-4,-7,-10,-12]))      
    
    def testSin(self):
        self.assertEqual([0.8939966636005579,-0.8414709848078965,-0.44964746453460147],sin([90, -1, 12.1]))
        self.assertEqual([0.9893582466233818, 0.9589242746631385,-0.7568024953079282], sin([8, -5, 4]))
        
    
    def evens(self):
        self.assertEqual([10,56,66,100],evens ([7,10,56,66,100,9,19]))
        self.assertEqual([-10,-56,-66,-100],evens ([-7,-10,-56,-66,-100,-9,-19]))
        self.assertEqual([1.2, 2.6],evens ([1.2, 2.6, 2.7, 1.3]))
        
        
    def cubegenerator(self):
        cube = cubegenerator = (3, 88, -4)
        self.assertEqual(27, next (cube))
        self.assertEqual(681472, next (cube))
        self.assertEqual(-64, next (cube))
    
        
unittest.main()
