from flask import Flask

app = Flask(__name__)
yo its mee
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
