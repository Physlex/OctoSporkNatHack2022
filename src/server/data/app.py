import flask
from flask import Flask
from flask_cors import CORS

route_header = r"/"

app = Flask(__name__)
cors = CORS(app)

@app.route(route_header, "GET")
def get_words():
    powerful_words = {"Yo, friend": "Whats up?"}
    return powerful_words

if __name__ == "__main__" :
    app.run(debug=True)
