from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main-page')
def mainPage():
    return render_template('main-page.html')

@app.route('/home')
def template():
    return render_template('template.html')