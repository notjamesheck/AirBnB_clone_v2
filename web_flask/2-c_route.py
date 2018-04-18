#!/usr/bin/python3
'''
    comment
'''
from flask import Flask
app = Flask(__name__)
'''
    comment
'''


@app.route('/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def web_flask():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route():
    text.replace(" ", "_")
    return 'C %s' % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
