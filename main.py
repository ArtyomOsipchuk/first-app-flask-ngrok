from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от Осипчука Артёма"


@app.route('/about')
def about():
    return 'Тест странички обо мне'


if __name__ == '__main__':
    app.run(host='', port=80)