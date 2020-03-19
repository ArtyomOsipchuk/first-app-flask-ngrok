from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/")
def index():
    return "Привет от Артёма"

@app.route("/test")
def index():
    return "Всё работает"


if __name__ == '__main__':
    app.run()