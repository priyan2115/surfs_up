from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
@app.route('/Home')
def Name():
    return "My Name Is Pri"

