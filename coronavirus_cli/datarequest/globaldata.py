import requests
from string import punctuation, maketrans
from bs4 import BeautifulSoup
from urls import BASE_URL

r = requests.get(BASE_URL)

# print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')
countries_tags = soup.find_all('a', class_="mt_a")

countries_raw = list(map(lambda x : x.get_text(), countries_tags))

transtab = str.maketrans('','',punctuation) # mapping table to remove all punctuation

countries_normalize = map(lambda x : ''.join(list(map(str.capitalize, x.strip(".-").split()))) + '\n',countries_raw )


with open('countries.py', 'w') as f : 
    f.writelines(countries_normalize)