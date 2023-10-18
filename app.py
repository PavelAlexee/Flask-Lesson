from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # http://127.0.0.1:5000/
def print_hello():
    return render_template('index.html')


@app.route('/text/')  # http://127.0.0.1:5000/text/
def print_text():
    return '<h1>Some text!</h1>'


app.run()
