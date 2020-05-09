import unittest
from components.Gates import *


class NOT_TestsCase(unittest.TestCase):
    def test_basic(self):
        value = False
        gate = NOT(False)
        self.assertTrue(gate())
        gate = NOT(True)
        self.assertFalse(gate())

    def test_inside(self):
        gate = NOT(NOT(False))
        self.assertFalse(gate())

class AND_TestCases(unittest.TestCase):
    
    def test_truthTable(self):
        valuesA = [False, True, False, True]
        valuesB = [False, False, True, True]
        results = [False,False,False,True]
    
        for truth in range(len(results)):
            gate = AND(valuesA[truth], valuesB[truth])
            self.assertEqual(gate(), results[truth])

    def test_inside(self):
        gate = AND(AND(True, True))
        self.assertTrue(gate())
        gate = AND(AND(False, True))
        self.assertTrue(gate())
    
    def test_listParameter(self):
        gate = AND([True, True])
        self.assertTrue(gate())
        
        gate = AND((True, True))
        self.assertTrue(gate())
        


        
unittest.main()