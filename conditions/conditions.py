#imports a calendar of sorts, this is a python module, very easy way to get current date
import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    #defining variable called "now" to "datetime.datetime.now()" this is just pythons way of getting the current date
    now = datetime.datetime.now()

    #define boolean variable called "new_year", whether or not its new year or not
    new_year = now.month == 1 and now.day == 1
    return render_template("newyear.html", new_year=new_year)