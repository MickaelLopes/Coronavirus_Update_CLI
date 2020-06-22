import requests
import urls
from string import punctuation
from bs4 import BeautifulSoup


class GlobalData():
    def __init__(self, test_url = None):
        if test_url: 
            self.soup = BeautifulSoup(open(test_url), 'html_parser')
        else: 
            self.r = requests.get(urls.World)
            if self.r.status_code == 200 : 
                self.soup = BeautifulSoup(r.text, 'html.parser')\
            else : 
                print('Cannot access the webpage')
                sys.exit(1)

    def get_number_cases(self, country='World'): 
        pass

    def get_number_active_case(self, country='World'): 
        pass

    def get_number_revover(self, country='World'):
        pass

    def get_number_death(self, country='World'): 
        pass
    