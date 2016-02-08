from flask import Flask
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
