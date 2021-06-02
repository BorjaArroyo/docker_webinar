import json
import sys

from flask import Flask, request
import argparse
import requests

app = Flask(__name__)


@app.route('/dummy')
def dummy():
    print('Dummy request received on flask2', file=sys.stderr)
    return 'OK'


@app.route('/save', methods=['POST'])
def redirection():
    body = request.json
    with open('example.json', 'w') as f:
        json.dump(body, f)
    return 'OK'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0', help='Specify the host of the application')
    parser.add_argument('--port', default=5000, help='Specify the port of the application')
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug=False)
