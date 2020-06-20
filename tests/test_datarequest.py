from datarequest.utils import _normalize_string
import unittest

class unittest_datarequest(unittest.TestCase): 
    
    def test_normalize_string(self):
        self.assertEqual(_normalize_string('USA'), 'USA')        
        self.assertEqual(_normalize_string('S. Korea'), 'SKorea')
        self.assertEqual(_normalize_string('portugal'), 'Portugal')
        self.assertEqual(_normalize_string('new zealand'), 'NewZealand')


unittest.main()