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


@app.route('/hbnb', strict_slas_es=False)
def web_flask():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text.replace(" ", "_")
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
