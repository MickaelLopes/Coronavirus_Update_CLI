# from .context import *
from cleo import Command
from datarequest.global_data import GlobalData
from tabulate import tabulate
import sys

with open('datarequest/countries.txt', 'r') as f:
    list_countries = f.readlines()
    list_countries = list(map(lambda x : x.strip('\n'), list_countries))

class RequestCommand(Command):
    """
    Request Command 

    request
        { --c|case : number of cases}
        { --t|active : number of active cases}
        { --r|recover : number of recover cases}
        { --d|death : number of deaths}
        { --p|country : data from specific country}
        { --l|list : display list of countries }
    """ 
    def handle(self):    
        corona_data = GlobalData()
        data = []
        show_all_values = False
        if self.option('list'):
            self.line('\n'.join(list_countries))
            sys.exit()
        if self.option('country'): 
            question =self.create_question('Target country ?', default = 'USA')
            question.set_autocomplete_values(list_countries)
            choice = self.ask(question)
            # self.line("Choose among the list of given countries : \n")
            # self.line('\t'.join(list_countries))
            country = choice
            self.line(f'\nData for country {country}\n')
        if not(self.option('country')):
            country = 'World'
            self.line('\nWorld data\n')
        if not(self.option('case')) and not(self.option('active')) and not(self.option('recover')) and not(self.option('death')):
            show_all_values = True
        if self.option('case') or show_all_values : 
            data.append(['Total Cases', corona_data.get_number_cases(country = country)])
        if self.option('active') or show_all_values:
            data.append(['Active Cases', corona_data.get_number_active_case(country = country)])
        if self.option('recover') or show_all_values:
            data.append(['Recovered Cases', corona_data.get_number_recover(country = country)]) 
        if self.option('death') or show_all_values:
            data.append(['Deaths', corona_data.get_number_death(country = country)])
        print(tabulate(data))
