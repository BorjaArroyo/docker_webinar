import sys

from flask import Flask
import argparse
import requests

app = Flask(__name__)


@app.route('/dummy')
def dummy():
    print('Dummy request received on flask1', file=sys.stderr)


@app.route('/redirection_and_save')
def redirection_and_file_save():
    body = {'example_key': 'example_value'}
    response = requests.post('http://flask2:80/save', json=body)
    print('Json object sent to the other flask', file=sys.stderr)
    return 'OK'


@app.route('/redirection')
def redirection():
    response = requests.get('http://flask2:80/dummy')
    return 'OK'


@app.route('/redirection_and_persist')
def redirection_and_persist():
    body = {'example_key': 'example_value'}
    response = requests.post('http://flask3:80/save', json=body)
    print('Json object sent to the other flask', file=sys.stderr)
    return 'OK'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0', help='Specify the host of the application')
    parser.add_argument('--port', default=5000, help='Specify the port of the application')
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug=False)
