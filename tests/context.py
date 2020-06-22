"""
Insert the project library as local package direcotry in order to be able to call the function for testing and provide path for testing ressources
"""

import os
import sys

test_ressources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests_resources'))
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


sys.path.insert(0,project_path)

TEST_WORLD_URL = test_ressources_path + '/Worldometers_MainPage.html'