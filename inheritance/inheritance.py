#This file is for inheritance 

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home1.html")

@app.route("/more")
def more():
    return render_template("more1.html")