import mysql.connector

connection = mysql.connector.connect(host='localhost',database='mysql',user='root',password='ppp')
cursor = connection.cursor()

statement = "SELECT counterparty_id FROM db_grad_cs_1917.counterparty WHERE counterparty_name = 'Lewis'"

counterparty = cursor.execute(statement, multi=True)
for result in cursor.execute(statement, multi=True):
    print("HERE")
    res = result.fetchone()
    print(res[0])
    # for x in res:
    #     print(x)

