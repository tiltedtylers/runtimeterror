from flask import Flask, Response
from flask_cors import CORS
import requests
import webServiceStream
from RandomDealData import *
import mysql.connector

connection = mysql.connector.connect(host='localhost',database='mysql',user='root',password='ppp')
cursor = connection.cursor()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    username = requests.args.get('username')
    password = requests.args.get('password')
    # username = 'aliso3n'
    # password = 'pass2'

    if (len(username) < 0 or len(password) < 0):
        return False # Don't allow signup with empty user/pass

    select_stmt = (
        "select * from db_grad_cs_1917.users where user_id = '" +
        username + "'"
    )
    for result in cursor.execute(select_stmt, multi=True):
        res = result.fetchone()
        if res == None:
            # INSERT
            insert_stmt = (
                "INSERT INTO db_grad_cs_1917.users (user_id, user_pwd) "
                "VALUES ('" + username + "', '" + password + "')"
            )
            cursor.execute(insert_stmt)
            connection.commit()
        return True

signup()

# @app.route('/login', methods=['GET', 'POST'])
def signin():
    username = requests.args.get('username')
    password = requests.args.get('password')
    # username = 'aliso3n'
    # password = 'pass2'

    if (len(username) < 0 or len(password) < 0):
        return False # Don't allow sign in with empty user/pass

    select_stmt = (
        "select * from db_grad_cs_1917.users where user_id = '" +
        username + "'"
    )
    for result in cursor.execute(select_stmt, multi=True):
        res = result.fetchone()
        if res == None:
            return False
        if res[1] != password:
            return False
        return True
