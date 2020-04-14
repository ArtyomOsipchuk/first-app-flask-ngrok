from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/")
def index():
    return "Привет от Осипчука Артёма"


@app.route("/test")
def F():
    return "testing >:3"


if __name__ == '__main__':
    app.run(host='', port=80)