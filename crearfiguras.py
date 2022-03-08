import pandas as pd # import Pandas library 
from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://admin:1qaz2wsx3edcqwerty@bdesp2021.cb6go1meri4l.us-east-2.rds.amazonaws.com/STORE") #info de nuestra BD en AWS
query="SELECT pais,COUNT( * ) SKU FROM sales GROUP BY pais LIMIT 5" #query de sql obtiene una tabla con pais y el conteo de los SKU (Ventas por país)
df = pd.read_sql(query,my_conn) #se define el dataframe con la consulta de sql

lb= [row for row in df['pais']] # Labels/ los nombres que se muestran en el pie chart
plot=df.plot.pie(title="pais",y='SKU',labels=lb,autopct='%1.0f%%') #y= qué valores van dentro del pie chart
fig = plot.get_figure() #genera la figura
fig.savefig("piechart.png") #guarda la figura en la misma carpeta que este archivo .py

plot=df.plot.bar(x="pais",y='SKU',rot=0)
fig = plot.get_figure()
fig.savefig("bar.png")

plot=df.plot.scatter(x="pais",y='SKU',c='Red')

fig = plot.get_figure()
fig.savefig("scatter.png")