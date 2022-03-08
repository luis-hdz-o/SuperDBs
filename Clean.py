import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

import numpy as np 
import matplotlib.pyplot as plt 
import statsmodels.api as sm 
import glob

empdata = pd.read_csv('retail.csv', index_col=False, delimiter = ',')
print(empdata.head())