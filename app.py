import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def main():
    print ('Request')
    print (request)
    print ('RAW Data')
    print (request.get_data())
    print ('Request Arguments')
    print (request.args)
    print ('Form Data')
    print (request.form)
    print ('Request Files')
    print (request.files)
    print ('Request Values')
    print (request.values)
    print ('Request JSON')
    print (request.json)
    response = app.response_class(
        response = 'success',
        status = 200,
        mimetype = 'application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)