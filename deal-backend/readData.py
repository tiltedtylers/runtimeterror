import requests
import json

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