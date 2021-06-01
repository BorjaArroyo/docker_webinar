import sys

from flask import Flask
import argparse
import requests

app = Flask(__name__)


@app.route('/dummy')
def dummy():
    print('Dummy request received', file=sys.stderr)


@app.route('/redirection_and_save')
def redirection_and_file_save():
    body = {'example_key': 'example_value'}
    response = requests.post('http://flask2:80/save', json=body)
    print('Dummy request received', file=sys.stderr)


@app.route('/redirection')
def redirection():
    response = requests.get('http://flask2:80/dummy')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0', help='Specify the host of the application')
    parser.add_argument('--port', default=5000, help='Specify the port of the application')
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug=False)
