import requests
import json
import mysql.connector
import datetime

connection = mysql.connector.connect(host='localhost',database='mysql',user='root',password='ppp')
cursor = connection.cursor()

r = requests.get('http://localhost:8080/streamTest', stream=True)

def eventStream():
    for line in r.iter_lines(chunk_size=1):
        if line:
            yield '{}\n\n'.format(line.decode())

mystr = next(eventStream())
mystr = json.loads(mystr)

def insert_query(data):
    statement = "SELECT deal_id FROM db_grad_cs_1917.deal ORDER BY deal_id DESC LIMIT 1"
    for result in cursor.execute(statement, multi=True):
        res = result.fetchone()
        id = str(res[0] + 1)

    time = data["time"]
    time = datetime.datetime.strptime(time, '%d-%b-%Y (%H:%M:%S.%f)')
    time = str(time.isoformat())

    statement = "SELECT counterparty_id FROM db_grad_cs_1917.counterparty WHERE counterparty_name='" + data["cpty"] + "'"
    for result in cursor.execute(statement, multi=True):
        res = result.fetchone()
        counterparty = res[0]

    statement = "SELECT instrument_id FROM db_grad_cs_1917.instrument WHERE instrument_name='" + data["instrumentName"] + "'"
    for result in cursor.execute(statement, multi=True):
        res = result.fetchone()
        instrument = res[0]

    deal_type = data["type"]
    amount = data["price"]
    quantity = data["quantity"]

    sql_insert = "Insert into db_grad_cs_1917.deal " \
                 "VALUES(" + id + ", '" + time + "', " + str(counterparty) + ", " + str(instrument) + ", '" + deal_type + "', " + str(round(amount, 2)) + ", " + str(quantity) +")"
    print(sql_insert)
    cursor.execute(sql_insert)
    connection.commit()

insert_query(mystr)
