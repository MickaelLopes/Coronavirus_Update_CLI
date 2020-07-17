# Coronavirus CLI 

Project aim to provide a command line interface for update on the coronavirus cases in the World. 

The data are extracted from the Worldometers website (https://www.worldometers.info/coronavirus/)


## Prerequisites 
Please install the prerequisites libraries in your python environment before running the project 

``` python 
pip install requirements.txt
```

## Installation 

To install the package as script, just copy or clone the the repository in the target directory from which you want the script to run

## Usage

To make the default request in script mode, open terminal in the coronavirus_cli folder and enter the following command
```console
python main.py request
```
This will provide current data at the World level. The answer provided will be : 
```

World data

---------------  --------
Total Cases      13952529
Active Cases      5075419
Recovered Cases   8284343
Deaths             592767
---------------  --------
```

For more targeted data, here the list of arguments available are : 

| Argument Tag | Description 
| --- | --- |
| ``-p`` or ``--country``| Toggle to request data from a specific country |
| ``-l`` or ``--list`` | Display list of country availables| 
| ``-c`` or ``--case``| Toggle to request number of cases |
| ``-t`` or ``--active``| Toggle to request number of active cases |
| ``-r`` or ``--recover``| Toggle to request number of recovered cases |
| ``-d`` or ``--death``| Toggle to request number of deaths |

When using the tag ``-p`` or ``--country`` the systems will ask which country is requested. The user will prompt the target country (autofill functionality implemented). Only __one__  country can be requested. (see list of country via tag ``-l`` or ``--list)

For example, to get number of active and recovered cases from France : 
```console
python main.py request -p -t -r
Target country ? France

Data for country France

---------------  -----
Active Cases     64664
Recovered Cases  79036

```

## License
see License.md 