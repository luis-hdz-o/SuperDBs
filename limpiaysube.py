import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm 
import glob

import mysql.connector as msql
from mysql.connector import Error


#Cargar datos
url = 'retailfinal.csv'
#url = 'test2.csv'

df = pd.read_csv(url, index_col=False, delimiter = ',')
# print(df.head(5))
# print(df.shape)
# print(df.info())t
# print(df.describe())

#renombrar columnas
df=df.rename(columns={'Invoice': 'factura','StockCode':'SKU','Description':'descripcion','Quantity':'cantidad','InvoiceDate':'fechacompra','Price':'precioventa','Customer ID':'idcliente','Country':'pais'}) 
#print(df)

#cambiar al formato datetime de DD/MM/AAA a >> AAAA-MM-DD HH:MM:SS
df.fechacompra = pd.to_datetime(df["fechacompra"]).dt.strftime('%Y-%m-%d %H:%M:%S')

#cambiar el formato de las demás columnas
df=df.astype({'factura': 'Int64', 'SKU':'string', 'descripcion':'string', 'cantidad':'Int64', 'precioventa':'float64','idcliente': 'Int64', 'pais':'string'})


#remover los records con NANs
totalnan= df.isna().sum().sum()
total= len(df.index)
#print(total)
print("{} records con NaN fueron removidos, que son {:.2%} del total de records de la BD".format(totalnan, ((totalnan/total))))
df.dropna(inplace=True)
#print(df)

#conexion a la BD
try:
    #conn = msql.connect(host='bdesp2021.cb6go1meri4l.us-east-2.rds.amazonaws.com', user='admin',
                        #password='1qaz2wsx3edcqwerty')
    conn = msql.connect(host='localhost', user='root',
                        password='')
    if conn.is_connected():
    	cursor = conn.cursor()
    	# cursor.execute("select database();")
    	# record = cursor.fetchone()
    	# print("You're connected to database: ", record)
    for i, row in df.iterrows():
    	#here %S means string values
        #print(row['InvoiceDate'])
        # date_time= str(row['InvoiceDate'])
        # date_time= date_time.replace('/','-')
        # print(date_time)
    	sql = "INSERT INTO STORE.SALES (factura,SKU,descripcion,cantidad,fechacompra,precioventa,idcliente,pais) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    	#print(sql)
    	#print(tuple(row))
    	cursor.execute(sql, tuple(row))
    	#print("Record inserted")
    	# the connection is not auto committed by default, so we must commit to save our changes
    	conn.commit()
    	print("Progreso: {:.2%}".format(i/total), end= "\r")
except Error as e:
	print("Error while connecting to MySQL", e)

print("La base de datos se ha cargado exitosamente! Ahora ya puedes empezar con el trabajo de verdad")

'''
df=df.replace(to_replace=r'.\(.+\)$', value= '', regex= True)
# print(df.head(1))

df.fecha= df.fecha.replace(regex= {'Aemet': '', r'\.+xls': ''})
# print(df.head(1))
# print (df.info())

df=df.astype({'estacion': 'string','provincia': 'string', 'temp_max':'float64', 'temp_min':'float64', 'viento_racha':'float64', 'viento_vel_max':'float64','fecha': 'datetime64[ns]'})
df['fecha']=pd.to_datetime(df["fecha"].dt.strftime('%Y-%m-%d'))
df.info()

estaciones_con_nan= df[df.isnull().any(axis=1)]['estacion'].unique()
df.drop(df[df['estacion'].isin(estaciones_con_nan)].index, inplace= True)
df.isna().sum()
# print(df.isna().sum())
'''