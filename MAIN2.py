import pymysql
import csv
db = pymysql.connect("bdesp2021.cb6go1meri4l.us-east-2.rds.amazonaws.com","admin","1qaz2wsx3edcqwerty","TIENDITA" )

cursor = db.cursor()
csv_data = csv.reader(open('test2.csv'))
next(csv_data)
for row in csv_data:
    cursor.execute('INSERT INTO VENTAS2(col1,col2,col3,col4,col5,col6,col7,col8) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)',row)

db.commit()
cursor.close()