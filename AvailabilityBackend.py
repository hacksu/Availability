from flask import Flask, jsonify, request
from flask.ext.cors import CORS
import re
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

    json = request.get_json()
    if not json:
        return jsonify({"error": "not JSON"})

    if len(json) != 1:
        return jsonify({"error": "wrong len"})

    safe = {}
    for key in json:
        value = json[key]
        print(value, key)
        key = re.sub('[<>*&#@$;:]', '', key)

        value = re.sub('[<>*&#@;:]', '', value)
        print(value, key)
        if value == "Free" or value == "Busy" or value == "Putting out a fire" or value == "Running really fast":
            safe[key] = value

    availability.update(safe)
    return jsonify(availability)

if __name__ == "__main__":
    app.run(debug=True)
