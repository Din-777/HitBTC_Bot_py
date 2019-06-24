
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import pandas as pd
import queue

class Trading:

    inputData = None
    
    def __init__(self):
        pass 

    def updateData(self, df):
        self.df = df
        pass  


