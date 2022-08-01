from flask import Flask, Response, request, jsonify, render_template
from flask_cors import CORS
from backend.data.nat_muse import NatMuse

default_route_header = r"/"

# Flask and CORS
app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True

# Routing
@app.route(default_route_header, methods=["GET"])
def render_landing():
    return render_template("index.html")

@app.route('/muse/recording', methods=['GET'])
def get_muse_data() -> Response:
    args = request.args
    duration = args.get("duration", default="60", type=float)
    muse = NatMuse()
    muse.record(duration)
    return jsonify(["An arbitrary list!"])

if __name__ == "__main__" :
    app.run(debug=True)
