from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello.. Working!"


app.run(host="0.0.0.0")