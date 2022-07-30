import flask
from flask import Flask
from flask_cors import CORS
from nat_muse import Muse

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def postME():
    data = flask.request.get_json()
    data = flask.jsonify(data)
    return data

if __name__ == "__main__" :
    app.run(debug=True)
