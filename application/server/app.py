from flask import Response
from quart import Quart, ResponseReturnValue, request, jsonify, render_template
from backend.data.nat_muse import NatMuse

default_route_header = r"/"

# Flask and CORS
app = Quart(__name__)
app.config["DEBUG"] = True

# Routing
@app.route(default_route_header, methods=["GET"])
def get_words():
    return render_template("index.html")

@app.route('/muse/recording', methods=['GET'])
def get_muse_data() -> Response:
    args = request.args
    duration = args.get("duration", default="60", type=float)
    muse = NatMuse()
    muse.record(duration)
    return jsonify(["An arbitrary list!"])

@app.route('/muse/connecting', methods=['GET'])
def connect_to_muse() -> Response:
    args = request.args
    muse_id = args.get("muse_id", default="0", type=int)
    muse = NatMuse()
    muse.connect(0)
    list_2d = [
        [muse_id], ["Muse connection finished"]
    ]
    return jsonify(list_2d)

if __name__ == "__main__" :
    app.run(debug=True)
