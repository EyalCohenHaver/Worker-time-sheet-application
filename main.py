from worker import Worker
from time import sleep
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'home'

@app.route('/new-worker')
def index():
    return f'new-worker'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)