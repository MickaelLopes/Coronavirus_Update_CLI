import sys
import unittest

import context
from coronavirus_cli.datarequest.utils import _normalize_country_name

# print(sys.path)
class unittest_datarequest(unittest.TestCase): 
    
    def test_normalize_string(self):
        self.assertEqual(_normalize_country_name('USA'), 'USA')        
        self.assertEqual(_normalize_country_name('S. Korea'), 'S_Korea')
        self.assertEqual(_normalize_country_name('portugal'), 'Portugal')
        self.assertEqual(_normalize_country_name('new zealand'), 'New_Zealand')
