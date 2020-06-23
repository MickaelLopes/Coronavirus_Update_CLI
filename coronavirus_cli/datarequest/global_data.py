import requests
import sys
from string import punctuation
from bs4 import BeautifulSoup
from .urls import *
from .utils import _find_country_row

class GlobalData():
    def __init__(self, test_url = None):
        if test_url: 
            self.soup = BeautifulSoup(open(test_url), 'html.parser')
        else: 
            self.r = requests.get(World)
            if self.r.status_code == 200 : 
                self.soup = BeautifulSoup(self.r.text, 'html.parser')
            else: 
                print('Cannot access the webpage')
                sys.exit(1)

    def get_number_cases(self, country='World'): 
        if country == 'World': 
            world_el = self.soup.find('td', string="World")
            world_row = world_el.parent.find_all('td')
            
            # Hardcodes position of the number case column 
            number_case = int(world_row[2].string.replace(',',''))
            return number_case
        else : 
            country_row, _ = _find_country_row(self.soup, country)
            number_case = int(country_row[2].string.replace(',',''))
            return number_case

    def get_number_active_case(self, country='World'): 
        if country == 'World': 
            world_el = self.soup.find('td', string="World")
            world_row = world_el.parent.find_all('td')
            
            # Hardcodes position of the number case column 
            number_case = int(world_row[8].string.replace(',',''))
            return number_case
        else : 
            country_row, _ = _find_country_row(self.soup, country)
            number_case = int(country_row[8].string.replace(',',''))
            return number_case

    def get_number_revover(self, country='World'):
        if country == 'World': 
            world_el = self.soup.find('td', string="World")
            world_row = world_el.parent.find_all('td')
            
            # Hardcodes position of the number case column 
            number_case = int(world_row[6].string.replace(',',''))
            return number_case
        else : 
            country_row, _ = _find_country_row(self.soup, country)
            number_case = int(country_row[6].string.replace(',',''))
            return number_case


    def get_number_death(self, country='World'): 
        if country == 'World': 
            world_el = self.soup.find('td', string="World")
            world_row = world_el.parent.find_all('td')
            
            # Hardcodes position of the number case column 
            number_case = int(world_row[4].string.replace(',',''))
            return number_case
        else : 
            country_row, _ = _find_country_row(self.soup, country)
            number_case = int(country_row[4].string.replace(',',''))
            return number_case

    