from flask import Flask, Response
from flask_cors import CORS
from flask import request
import webServiceStream
from RandomDealData import *

import mysql.connector

connection = mysql.connector.connect(host='localhost',database='mysql',user='root',password='ppp')
cursor = connection.cursor()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return webServiceStream.index()

@app.route('/testservice')
def testservice():
    return webServiceStream.testservice()

@app.route('/streamTest')
def stream():
    return webServiceStream.stream()

@app.route('/streamTest/sse')
def sse_stream():
     return webServiceStream.sse_stream()

@app.route('/dbconnect')
def dbconnect():
    sql = "SELECT NOW()"
    cursor.execute(sql)
    data=cursor.fetchall()
    print(data)
    if(len(data) > 0):
        return Response( "true", status=200, mimetype='application/json')
    return Response( "false", status=400, mimetype='application/json')

@app.route('/login',methods = ['GET','POST'])
def login():
    username= request.args.get('username')
    password = request.args.get('password')
    sql = "SELECT * FROM db_grad_cs_1917.users WHERE users.user_id=%s and users.user_pwd=%s"
    cursor.execute(sql, (username,password))
    data = cursor.fetchall()
    print(data)
    if(len(data) > 0):
        return Response( "true", status=200, mimetype='application/json')
    return Response( "false", status=400, mimetype='application/json')


def bootapp():
    #global rdd 
    #rdd = RandomDealData()
    #webServiceStream.bootServices()
    app.run(debug=True, port=8080, threaded=True, host=('0.0.0.0'))


if __name__ == "__main__":
      bootapp()
