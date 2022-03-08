import pandas as pd # import Pandas library 
from sqlalchemy import create_engine

my_conn = create_engine("mysql+mysqldb://admin:1qaz2wsx3edcqwerty@bdesp2021.cb6go1meri4l.us-east-2.rds.amazonaws.com/STORE") #info de nuestra BD en AWS

query="SELECT pais, sum(cantidad*precioventa) as cantidad FROM sales GROUP BY MONTH(fechacompra);" #query de sql obtiene una tabla con factura y el conteo de los SKU (Ventas por país)
df = pd.read_sql(query,my_conn) #se define el dataframe con la consulta de sql
print(df)

lb= [row for row in df['pais']] # Labels/ los nombres que se muestran en el pie chart
plot=df.plot.pie(title="pais",y='cantidad',labels=lb,autopct='%1.0f%%') #y= qué valores van dentro del pie chart
fig = plot.get_figure() #genera la figura
fig.savefig("piechart.png") #guarda la figura en la misma carpeta que este archivo .py

plot=df.plot.bar(x="pais",y='cantidad',rot=0, figsize= (3,5))
fig = plot.get_figure()
fig.savefig("barventas.png")


plot=df.plot.scatter(x="pais",y="cantidad",rot=0,c='Red', figsize= (3,5))
fig = plot.get_figure()
fig.savefig("scatterventas.png")
