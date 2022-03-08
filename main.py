import pymysql

def mysqlconnect():
	conn = pymysql.connect(
		host = 'bdesp2021.cb6go1meri4l.us-east-2.rds.amazonaws.com',
		user = 'admin',
		password= "1qaz2wsx3edcqwerty",
		db = 'TIENDITA',
	)

	cur = conn.cursor()
	cur.execute("select @@version")
	output = cur.fetchall()
	print(output)

	conn.close()

if __name__ == "__main__":
	mysqlconnect()