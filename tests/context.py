"""
Insert the project library as local package direcotry in order to be able to call the function for testing 
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
