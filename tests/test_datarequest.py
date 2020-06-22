import sys
import unittest
import context
import requests
from coronavirus_cli.datarequest.utils import _normalize_country_name
from coronavirus_cli.datarequest.global_data import GlobalData
from coronavirus_cli.datarequest import urls
from bs4 import BeautifulSoup

class unittest_utils_function(unittest.TestCase): 
    """
    Basic Testing for the utils function in the datarequest module
    """

    def test_normalize_string(self):
        self.assertEqual(_normalize_country_name('USA'), 'USA')        
        self.assertEqual(_normalize_country_name('S. Korea'), 'S_Korea')
        self.assertEqual(_normalize_country_name('portugal'), 'Portugal')
        self.assertEqual(_normalize_country_name('new zealand'), 'New_Zealand')

class unittest_connectivity(unittest.TestCase):
    """
    Test the connectivity to request the url and parsed them with beautifoul soup
    """

    def setUp(self): 
        self.r_test = requests.get(urls.World)
    
    def test_connectivity(self): 
         self.assertEqual(self.r_test.status_code, 200)

    def test_parsing(self): 
        try: 
            test_soup = BeautifulSoup(self.r_test.text, 'html.parser')
        except : 
            test_parsing_successful = False
        else : 
            test_parsing_successful = True
        self.assertEqual(test_parsing_successful,True)
class unittest_global_data(unittest.TestCase): 
    """
    Testing of the world_data module meant to extract data from world webpage 
    """

    def setUp(self): 
        # self.soup_world_test = BeautifulSoup(open(context.TEST_WORLD_URL), 'html.parser')
        self.test_global_world = GlobalData(test_url=context.TEST_WORLD_URL)
    def test_world_data(self): 
        self.assertEqual(self.test_global_world.get_number_cases(), 9051535)
        self.assertEqual(self.test_global_world.get_number_active_case(), 3738783)
        self.assertEqual(self.test_global_world.get_number_revover(), 4841948)
        self.assertEqual(self.test_global_world.get_number_death(), 470804)
        
    def test_country_data_USA(self): 
        self.assertEqual(self.test_global_world.get_number_cases(country='USA'), 2356657)
        self.assertEqual(self.test_global_world.get_number_active_case(country='USA'), 1254055)
        self.assertEqual(self.test_global_world.get_number_revover(country='USA'), 980355)
        self.assertEqual(self.test_global_world.get_number_death(country='USA'), 122247)
    
    def test_country_data_South_Korea(self): 
        self.assertEqual(self.test_global_world.get_number_cases(country='S_Korea'), 12438)
        self.assertEqual(self.test_global_world.get_number_active_case(country='S_Korea'), 1277)
        self.assertEqual(self.test_global_world.get_number_revover(country='S_Korea'), 10881)
        self.assertEqual(self.test_global_world.get_number_death(country='S_Korea'), 280)
    
    def test_country_data_Trinidad_And_Tobago(self): 
        self.assertEqual(self.test_global_world.get_number_cases(country='Trinidad_And_Tobago'), 123)
        self.assertEqual(self.test_global_world.get_number_active_case(country='Trinidad_And_Tobago'), 6)
        self.assertEqual(self.test_global_world.get_number_revover(country='Trinidad_And_Tobago'), 109)
        self.assertEqual(self.test_global_world.get_number_death(country='Trinidad_And_Tobago'), 8)
    
