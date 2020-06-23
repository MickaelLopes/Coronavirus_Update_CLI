import sys
import unittest
import context
import requests

from coronavirus_cli.datarequest.utils import _normalize_country_name, _find_country_row
from coronavirus_cli.datarequest.global_data import GlobalData
from coronavirus_cli.datarequest import urls
from bs4 import BeautifulSoup

class unittest_utils_function(unittest.TestCase): 
    """
    Basic Testing for the utils function in the datarequest module
    """

    def setUp(self):
        self.test_global = GlobalData(test_url=context.TEST_WORLD_URL)

    def test_normalize_string(self):
        self.assertEqual(_normalize_country_name('USA'), 'USA')        
        self.assertEqual(_normalize_country_name('S. Korea'), 'S_Korea')
        self.assertEqual(_normalize_country_name('portugal'), 'Portugal')
        self.assertEqual(_normalize_country_name('new zealand'), 'New_Zealand')
    
    def test_find_country_row(self):
        _ , test_country_USA = _find_country_row(self.test_global.soup, 'USA')
        _ , test_country_Sao_tome = _find_country_row(self.test_global.soup, 'Sao_Tome_And_Principe')
        _ , test_country_South_korea= _find_country_row(self.test_global.soup, 'S_Korea')

        self.assertEqual(test_country_USA, 'USA')
        self.assertEqual(test_country_Sao_tome, 'Sao Tome and Principe')
        self.assertEqual(test_country_South_korea, 'S. Korea')
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

class unittest_global_data_world(unittest.TestCase): 
    """
    Testing of the global_data and extract data from world  
    """

    def setUp(self):
        self.test_global_world = GlobalData(test_url=context.TEST_WORLD_URL)
        
    def test_world_data_total_cases(self):
        self.assertEqual(self.test_global_world.get_number_cases(), 9051535)
    def test_world_data_active_cases(self):
        self.assertEqual(self.test_global_world.get_number_active_case(), 3738783)
    def test_world_data_revover_cases(self):
        self.assertEqual(self.test_global_world.get_number_revover(), 4841948)
    def test_world_data_death_cases(self): 
        self.assertEqual(self.test_global_world.get_number_death(), 470804)

class unittest_global_data_USA(unittest.TestCase):
    """
    Testing of the global_data and extract data from USA
    """
    def setUp(self):
        self.test_global_USA = GlobalData(test_url=context.TEST_WORLD_URL)

    def test_world_data_total_cases(self):
        self.assertEqual(self.test_global_USA.get_number_cases(country='USA'), 2356657)
    def test_world_data_active_cases(self):
        self.assertEqual(self.test_global_USA.get_number_active_case(country='USA'), 1254055)
    def test_world_data_revover_cases(self):
        self.assertEqual(self.test_global_USA.get_number_revover(country='USA'), 980355)
    def test_world_data_death_cases(self): 
        self.assertEqual(self.test_global_USA.get_number_death(country='USA'), 122247)

class unittest_global_data_South_Korea(unittest.TestCase):
    """
    Testing of the global_data and extract data from S Korea
    """
    def setUp(self):
        self.test_global_South_Korea = GlobalData(test_url=context.TEST_WORLD_URL)

    def test_world_data_total_cases(self):
        self.assertEqual(self.test_global_South_Korea.get_number_cases(country='S_Korea'), 12438)
    def test_world_data_active_cases(self):
        self.assertEqual(self.test_global_South_Korea.get_number_active_case(country='S_Korea'), 1277)
    def test_world_data_revover_cases(self):
        self.assertEqual(self.test_global_South_Korea.get_number_revover(country='S_Korea'), 10881)
    def test_world_data_death_cases(self): 
        self.assertEqual(self.test_global_South_Korea.get_number_death(country='S_Korea'), 280)
        

class unittest_global_data_Tri_Tob(unittest.TestCase):
    """
    Testing of the global_data and extract data from Trinidad and tobago
    """
    def setUp(self):
        self.test_global_Trinidad_and_Tobago = GlobalData(test_url=context.TEST_WORLD_URL)
    
    def test_world_data_total_cases(self):
        self.assertEqual(self.test_global_Trinidad_and_Tobago.get_number_cases(country='Trinidad_And_Tobago'), 123)
    def test_world_data_active_cases(self):
        self.assertEqual(self.test_global_Trinidad_and_Tobago.get_number_active_case(country='Trinidad_And_Tobago'), 6)
    def test_world_data_revover_cases(self):
        self.assertEqual(self.test_global_Trinidad_and_Tobago.get_number_revover(country='Trinidad_And_Tobago'), 109)
    def test_world_data_death_cases(self):
        self.assertEqual(self.test_global_Trinidad_and_Tobago.get_number_death(country='Trinidad_And_Tobago'), 8)
    
