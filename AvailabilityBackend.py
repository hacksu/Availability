from flask import Flask, jsonify
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return jsonify({"message": "Hello World!"})


@app.route("/availability")
def get_availability():
    return jsonify({"isaac": "free", "timothy": "kind of busy"})

if __name__ == "__main__":
    app.run(debug=True)
