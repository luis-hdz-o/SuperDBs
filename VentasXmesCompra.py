import pandas as pd # import Pandas library 
from sqlalchemy import create_engine
from datetime import datetime


my_conn = create_engine("mysql+mysqldb://admin:1qaz2wsx3edcqwerty@bdesp2021.cb6go1meri4l.us-east-2.rds.amazonaws.com/STORE") #info de nuestra BD en AWS

query="SELECT YEAR(fechacompra) as AÑO, MONTH(fechacompra) as MES, COUNT(DISTINCT factura) as VENTAS FROM sales GROUP BY MONTH(fechacompra), YEAR(fechacompra);" #query de sql obtiene una tabla con factura y el conteo de los SKU (Ventas por país)
df = pd.read_sql(query,my_conn) #se define el dataframe con la consulta de sql
#print(df)
'''
lb= [row for row in df['MES']] # Labels/ los nombres que se muestran en el pie chart
plot=df.plot.pie(title="MES",y='VENTAS',labels=lb,autopct='%1.0f%%') #y= qué valores van dentro del pie chart
fig = plot.get_figure() #genera la figura
fig.savefig("piechartventasmes.png") #guarda la figura en la misma carpeta que este archivo .py

plot=df.plot.bar(x="AÑO",y='VENTAS',rot=0, figsize= (10,5), stacked=True)
fig = plot.get_figure()
fig.savefig("barventasmes.png")


plot=df.plot.scatter(x="MES",y="VENTAS",rot=0,c='Red')
fig = plot.get_figure()
fig.savefig("scatterventasmes.png")
'''

plot= df.pivot(index='MES', columns= 'AÑO').plot(figsize= (10,5), stacked=True)
#plot=df.plot(index='MES', columns= 'VENTAS', figsize= (20,5), stacked=True)
fig = plot.get_figure()
fig.savefig("areaventasmes.png")