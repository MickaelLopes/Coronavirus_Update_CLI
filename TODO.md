# Data Access part
- [x] Collect list of countries and their associated urls pages 
- [x] Access world cases from test ressources page
- [x] Access USA case from test ressources page
    - [x] Create function which identify the good row for a given country (match the urls of the country with href tag ?)
            See utils.py

# Issue : Columns not tagged (which one is active case, death, etc ... ). Information only available in table header
    - [x] 1st impl. : Hard code the position of the columns (not dynamic, issue if defautl columsn order changes)
    - [ ] 2nd impl. : Create utils function which read the header and identify the column index for each data
    
# Testing 
- [x] Put in place a unit testing scenario
- [x] Unit testing for utils function in datarequest package

# Interfarce 