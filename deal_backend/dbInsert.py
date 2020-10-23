import requests
import json
import mysql.connector


import mysql.connector
connection = mysql.connector.connect(host='localhost',database='mysql',user='root',password='ppp')
cursor = connection.cursor()

r = requests.get('http://localhost:8080/streamTest', stream=True)

def eventStream():
    for line in r.iter_lines(chunk_size=1):
        if line:
            yield 'data:{}\n\n'.format(line.decode())

mystr = next(eventStream())
print(mystr)
mystr = mystr[5:]
print(mystr)
mystr = json.loads(mystr)
print(mystr)
print(mystr['instrumentName'])


def insert_query(dict):
    time = dict["time"]
    counterparty = cursor.execute("SELECT coutnerparty_id FROM db_grad_cs_1917.counterparty WHERE counterparty_name=" + dict["cpty"])
    instrument = cursor.execute("SELECT instrument_id FROM db_grad_cs_1917.instrument WHERE instrument_name=" + dict["instrumentName"])
    deal_type = dict["type"]
    amount = dict["price"]
    quantity = dict["quantity"]

    sql_insert = "Insert into db_grad_cs_1917.deal(deal_time, deal_counterparty_id, deal_instrument_id, deal_type, deal_amount, deal_quantity" \
                 "VALUES(" + time + ", " + counterparty + ", " + instrument + ", " + deal_type + ", " + amount + ", " + quantity +")"