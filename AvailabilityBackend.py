from flask import Flask, jsonify, request
from flask.ext.cors import CORS

availability = {}

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return jsonify({"message": "Hello World!"})


@app.route("/availability")
def get_availability():
    return jsonify(availability)


@app.route("/availability", methods=["POST"])
def record_availability():
    global availability

    availability.update(request.get_json())
    return jsonify(availability)

if __name__ == "__main__":
    app.run(debug=True)
