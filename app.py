from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = 'tnecniv'
    return render_template('home.html', name=name)

@app.route('/login')
def login():
    return render_template('login.html')