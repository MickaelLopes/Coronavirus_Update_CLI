# from .context import *
from cleo import Command
from datarequest.global_data import GlobalData


with open('datarequest/countries.txt', 'r') as f:
    list_countries = f.readlines()
    list_countries = list(map(lambda x : x.strip('\n'), list_countries))

class StartCommand(Command):
    """
    Start Command 

    start
        { --a|all : all data (case, active, recover, death)}
        { --c|case : number of cases}
        { --t|active : number of active cases}
        { --r|recover : number of recover cases}
        { --d|death : number of deaths}
        { --p|country : data from specific country}
    """ 
    def handle(self):
        
        self.line("Greetings and Welcome")
        corona_data = GlobalData()
        country = 'World'
        if self.option('country'): 
            question =self.create_question('which country ?', default = 'USA')
            question.set_autocomplete_values(list_countries)
            choice = self.ask(question)
            # self.line("Choose among the list of given countries : \n")
            # self.line('\t'.join(list_countries))
            country = choice

        if self.option('case') or self.option('all') : 
            print(f'Number of cases : \t{corona_data.get_number_cases(country = country)}')
        if self.option('active') or self.option('all'):
            print(f'Number of actives cases : \t {corona_data.get_number_active_case(country = country)}')
        if self.option('recover') or self.option('all'): 
            print(f'Number of recover cases : \t{corona_data.get_number_recover(country = country)}')
        if self.option('death') or self.option('all'):
            print(f'Number of death : \t {corona_data.get_number_death(country = country)}')
            