from flask import Flask, render_template, Response
from flask_sse import sse
from flask_cors import CORS
import requests
import time

import datetime
import json
import mysql.connector

connection = mysql.connector.connect(host='localhost',database='mysql',user='root',password='ppp')
cursor = connection.cursor()

app = Flask(__name__)
#app.register_blueprint(sse, url_prefix='/stream')
CORS(app)

## New function
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
    cursor.execute(sql_insert)
    connection.commit()

@app.route('/deals')
def forwardStream():
    r = requests.get('http://localhost:8080/streamTest', stream=True)
    def eventStream():
            for line in r.iter_lines( chunk_size=1):
                if line:
                    ## New code
                    data = json.loads(line)
                    insert_query(data)
                    ## End new code
                    yield 'data:{}\n\n'.format(line.decode())
    return Response(eventStream(), mimetype="text/event-stream")

@app.route('/client/testservice')
def client_to_server():
    r = requests.get('http://localhost:8080/testservice')
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

@app.route('/')
@app.route('/index')
def index():
    return "webtier service points are running..."


def get_message():
    """this could be any function that blocks until data is ready"""
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

def bootapp():
    app.run(port=8090, threaded=True, host=('0.0.0.0'))

if __name__ == '__main__':
     bootapp()
