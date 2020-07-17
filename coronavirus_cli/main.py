# !/usr/bin/env python3.7
from interface.command import RequestCommand
from cleo import Application

# from datarequest.global_data import GlobalData
# from datarequest.utils import _find_country_row
app = Application()
app.add(RequestCommand())

if __name__ == '__main__': 
    app.run()
    # g = GlobalData()
    # print(_find_country_row(g.soup, 'USA'))