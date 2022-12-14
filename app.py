import sys
from pathlib import Path
path = Path(__file__).parent.parent  # i.e. the folder above the tests folder, which has app
sys.path.append(path)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/test')
def say_hello():
    return('Another Dir for the flask app   ')

app.route('/devRoute')
def devRoute():
    return('Working on another branch')

if __name__ == '__main__':
    app.run()
