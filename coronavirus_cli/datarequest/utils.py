"""
List of utilities functions used in the datarequest package 
"""
from string import punctuation
import requests
from bs4 import BeautifulSoup
import sys

def _normalize_country_name(s : str):
    """
    Normalize a string by removing whitespace & punctuation and capitalize each word.

    Parameters:
        s(str) : String to be normalize

    Return: 
        _normalize_string(s)(str) : String normalized 
    """
    transtab = str.maketrans('','',punctuation) 
    list_s = s.split()
    new_list = []
    for el in list_s : 
        if el.isupper():
            el = el.translate(transtab) 
            new_list.append(el)
        else : 
            el = el.translate(transtab)
            el = el.capitalize()
            new_list.append(el)
    return '_'.join(new_list)


def _init_list_coutry(): 
    """
    Function to initialize the list of countries available in the CLI (see countries.py) and the dictionnary of the urls per countries (see urls.py)
    This function is made for iniatilization of the list only. It will read the list of countries and urls from the initial webpage ("https://www.worldometers.info/coronavirus/")
    """
    base_url = "https://www.worldometers.info/coronavirus/"
    r = requests.get(base_url)
    if r.status_code == 200: 
        soup = BeautifulSoup(r.text, 'html.parser')
        countries_tag = soup.find_all('a', class_='mt_a')
        
        # Create Dictionary country_name : country_url (key:value)
        countries_dict = {_normalize_country_name(x.get_text()):base_url + x['href'] for x in countries_tag }
        countries_dict['World'] = base_url

        # Sorting the dictionary by country name. In order to have the file sorted
        countries_dict_sorted = {x : countries_dict[x] for x in sorted(countries_dict.keys())}

        with open('countries.txt', 'w') as f : 
            list_countries = [x+'\n' for x in countries_dict_sorted.keys()]
            f.writelines(list_countries)
        with open('urls.py', 'w') as f : 
            list_urls = [f'{x} = "{y}"\n' for x,y in countries_dict_sorted.items()]
            f.writelines(list_urls)

    else : 
        print('Error when getting page')
        print(f'Page Status Code :{r.status_code}')
        sys.exit(1)
