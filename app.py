import flask
from flask import request
from flask import jsonify
import zipfile
import requests
from io import BytesIO
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def main():
    print 'Request Arguments \n\n'
    print request.args
    print 'Form Data \n\n'
    print request.form
    print 'Request Files \n\n'
    print request.files
    print 'Request Values \n\n'
    print request.values
    print 'Request JSON \n\n'
    print request.json
    response = app.response_class(
        response = 'success',
        status = 200,
        mimetype = 'application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)