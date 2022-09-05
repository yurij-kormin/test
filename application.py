from flask import render_template,Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, BIg World!</p>"



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
