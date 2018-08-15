import random
import time
import mysql.connector

mydb = mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "phpmyadmin/user",
	passwd = "phpmyadmin/password",
	database = "iot_device"	
)

#print(mydb)
mycursor = mydb.cursor()

'''
mycursor.execute("SHOW TABLES")

# show table name
for x in mycursor:
	print(x)
'''

# random insert values into database 
for i in range(0,5):
	no_one = str(random.randint(0,9))
	no_two = str(random.randint(0,99))

	sql = "INSERT INTO iot(iot_name, iot_value1, iot_value2) VALUES (%s, %s, %s)"
	val = ("TEMP", no_one, no_two)
	mycursor.execute(sql, val)

	mydb.commit()
	print(mycursor.rowcount, "record inserted.")
	time.sleep(5)

