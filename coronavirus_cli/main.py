#!/usr/bin/env python
from interface.command import StartCommand
from cleo import Application

# from datarequest.global_data import GlobalData
# from datarequest.utils import _find_country_row
app = Application()
app.add(StartCommand())

if __name__ == '__main__': 
    app.run()
    # g = GlobalData()
    # print(_find_country_row(g.soup, 'USA'))