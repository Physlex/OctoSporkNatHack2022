from flask import Flask, request, jsonify
from flask_cors import CORS
from muse_import import Stream

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def postME():
    data = request.get_json()
    data = jsonify(data)
    return data

if __name__ == "__main__" :
    my_stream = Stream()
    my_stream.connect()
    app.run(debug=True)