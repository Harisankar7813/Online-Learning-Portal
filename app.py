from flask import Flask, render_template,request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/base')
def base():
    return render_template("base.html")

if __name__ == "__main__": 
    app.run(debug=True)
