import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import statsmodels.api as sm 

file= 'countries.csv'
df= pd.read_csv(file, sep=";")
#print(df.head(5))

corr= df.set_index('alpa_3').corr()
sm.graphics.plot_corr(corr, xnames=list(corr.columns))
plt.show()
