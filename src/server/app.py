from crypt import methods
import flask
from flask import Flask, jsonify
from flask_cors import CORS

default_route_header = r"/"

app = Flask(__name__)
app.config["DEBUG"] = True

cors = CORS(app)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'
     }
]

@app.route(default_route_header, methods=["GET"])
def get_words():
    template_base =  "<h1>Distanct Reading Archive</h1><p>This site is a prototype</p>"
    return template_base

@app.route('/api/v1/resources/books/all', methods=['GET'])
def all():
    return jsonify(books)

if __name__ == "__main__" :
    app.run(debug=True)
