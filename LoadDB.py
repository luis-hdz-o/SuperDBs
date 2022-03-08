import pandas as pd
import mysql.connector as msql
from mysql.connector import Error


df = pd.read_csv('retail.csv', index_col=False, delimiter = ',')
df.head()


try:
    conn = msql.connect(host='bdesp2021.cb6go1meri4l.us-east-2.rds.amazonaws.com', user='admin',
                        password='1qaz2wsx3edcqwerty') #give ur username, password
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
    	#cursor.execute(sql, tuple(row))
    	print("Record inserted")
    	# the connection is not auto committed by default, so we must commit to save our changes
    	conn.commit()
except Error as e:
	print("Error while connecting to MySQL", e)