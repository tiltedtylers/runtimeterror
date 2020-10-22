import mysql.connector

connection = mysql.connector.connect(host='localhost', database='mysql', user='root',
                                     password='ppp', auth_plugin='mysql_native_password')
cursor = connection.cursor()

cursor.execute("SELECT * FROM db_grad_cs_1917.deal")

for deal in cursor:
    print(deal)

