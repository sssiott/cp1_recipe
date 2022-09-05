from flask import Flask, render_template, request, redirect, url_for,jsonify
from routes import search_route, login

app = Flask(__name__)
app.register_blueprint(search_route.bp)
app.register_blueprint(login.bp)

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template("home.html")


@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/signin_done')
def signin_done():
    return render_template("signin_done.html")