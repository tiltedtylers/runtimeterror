from flask import Flask, render_template, Response
from flask_sse import sse
from flask_cors import CORS
from flask import request
import requests
import time

app = Flask(__name__)
#app.register_blueprint(sse, url_prefix='/stream')
CORS(app)

@app.route('/dbconnect')
def dbconnect():
    dburl = "http://localhost:8080/dbconnect"
    r = requests.get(dburl)
    print(r)
    res_value = r.text
    return res_value

@app.route('/login',methods = ['GET','POST'])
def login():
    username = request.get_json()["username"]
    password = request.get_json()["password"]
    print(username,password)
    singupUrl = f"http://localhost:8080/login?username={username}&password={password}"
    r = requests.get(singupUrl)
    print(r)    
    res_value = r.text
    return res_value

@app.route('/deals')
def forwardStream():
    r = requests.get('http://localhost:8080/streamTest', stream=True)
    def eventStream():
            for line in r.iter_lines( chunk_size=1):
                if line:
                    yield 'data:{}\n\n'.format(line.decode())
    return Response(eventStream(), mimetype="text/event-stream")

@app.route('/client/testservice')
def client_to_server():
    r = requests.get('http://localhost:8080/testservice')
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

@app.route('/')
@app.route('/index')
def index():
    return "webtier service points are asdf running..."


def get_message():
    """this could be any function that blocks until data is ready"""
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

def bootapp():
    app.run(port=8090, threaded=True, host=('0.0.0.0'))

if __name__ == '__main__':
     bootapp()