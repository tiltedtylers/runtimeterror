import datetime
import requests
import json
import mysql.connector

# instrumentName = mystr['instrumentName']
# cpty = mystr['cpty']
# price = mystr['price']
# type = mystr['type']
# quantity = mystr['quantity']
# time = mystr['time']

connection = mysql.connector.connect(host='localhost',database='mysql',user='root',password='ppp')
cursor = connection.cursor()

r = requests.get('http://localhost:8080/streamTest', stream=True)

def eventStream():
    for line in r.iter_lines(chunk_size=1):
        if line:
            yield '{}'.format(line.decode())

mystr = next(eventStream())
# print(mystr)
# mystr = mystr[5:]
# print(mystr)
mystr = json.loads(mystr)
# print(mystr)
# print(mystr['instrumentName'])

# time = mystr["time"]
# print(time)
# print(datetime.datetime.strptime('21-Oct-2020', '%d-%b-%Y'))
# print(datetime.datetime.strptime('21-Oct-2020 (20:13:11.409362)', '%d-%b-%Y (%H:%M:%S.%f)'))
# print(datetime.datetime.strptime(time, '%d-%b-%Y (%H:%M:%S.%f)'))
# print(datetime.datetime.strptime('Jun 1 2005 1:33PM', '%b %d %Y %I:%M%p'))
# print(datetime("21-Oct-2020"))

def insert_query(dict):
    statement = "SELECT deal_id FROM db_grad_cs_1917.deal ORDER BY deal_id DESC LIMIT 1"
    for result in cursor.execute(statement, multi=True):
        res = result.fetchone()
        id = str(res[0] + 1)

    time = dict["time"]
    time = datetime.datetime.strptime(time, '%d-%b-%Y (%H:%M:%S.%f)')
    time = str(time.isoformat())

    statement = "SELECT counterparty_id FROM db_grad_cs_1917.counterparty WHERE counterparty_name='" + dict["cpty"] + "'"
    for result in cursor.execute(statement, multi=True):
        res = result.fetchone()
        counterparty = res[0]

    statement = "SELECT instrument_id FROM db_grad_cs_1917.instrument WHERE instrument_name='" + dict["instrumentName"] + "'"
    for result in cursor.execute(statement, multi=True):
        res = result.fetchone()
        instrument = res[0]

    deal_type = dict["type"]
    amount = dict["price"]
    quantity = dict["quantity"]

    sql_insert = "Insert into db_grad_cs_1917.deal " \
                 "VALUES(" + id + ", '" + time + "', " + str(counterparty) + ", " + str(instrument) + ", '" + deal_type + "', " + str(round(amount, 2)) + ", " + str(quantity) +")"
    print(sql_insert)
    cursor.execute(sql_insert)

insert_query(mystr)

connection.commit()
cursor.close()
connection.close()