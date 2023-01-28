from flask import Flask

app = Flask(__name__)
print("hello")
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
