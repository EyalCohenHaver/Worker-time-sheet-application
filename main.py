from worker import Worker
from time import sleep
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'hello'

@app.route('/')
def index():
    return f'hello'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)