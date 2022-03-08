import pandas as pd # import Pandas library 
from sqlalchemy import create_engine

import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot,plot
init_notebook_mode(connected=True)


my_conn = create_engine("mysql+mysqldb://admin:1qaz2wsx3edcqwerty@bdesp2021.cb6go1meri4l.us-east-2.rds.amazonaws.com/STORE") #info de nuestra BD en AWS

query="SELECT pais, COUNT(DISTINCT factura) as factura FROM sales WHERE pais = 'United Kingdom'" #query de sql obtiene una tabla con factura y el conteo de los SKU (Ventas por país)
df = pd.read_sql(query,my_conn) #se define el dataframe con la consulta de sql
print(df)

data = dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        locations = df['pais'],
        locationmode = "country names",
        z = df['factura'],
        text = df['pais'],
        colorbar = {'title' : 'Ventas por país'},
      )

layout = dict(title = 'Ventas por país',
              geo = dict(projection = {'type':'mercator'})
             )

choromap = go.Figure(data = [data],layout = layout)
choromap.show(renderer="png", width=800, height=300)

# iplot(choromap,validate=False)

'''
lb= [row for row in df['pais']] # Labels/ los nombres que se muestran en el pie chart
plot=df.plot.pie(title="pais",y='factura',labels=lb,autopct='%1.0f%%') #y= qué valores van dentro del pie chart
fig = plot.get_figure() #genera la figura
fig.savefig("piechart.png") #guarda la figura en la misma carpeta que este archivo .py

plot=df.plot.bar(x="pais",y='factura',rot=0)
fig = plot.get_figure()
fig.savefig("barventas.png")


plot=df.plot.scatter(x="pais",y="factura",rot=0,c='Red')
fig = plot.get_figure()
fig.savefig("scatterventas.png")
'''