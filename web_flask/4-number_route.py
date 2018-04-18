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
def c_route(text):
    text.replace(" ", "_")
    return 'C {}'.format(text)


@app.route('/python/(<text>)', strict_slashes=False)
def python_route(text=None):
    if text is None:
        text = 'is cool'
    text.replace(" ", "_")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    if type(n) is int:
        return '{} is a number'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
