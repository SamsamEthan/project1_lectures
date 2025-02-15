from flask import Flask, render_template

app = Flask(__name__)

#When using templates, make sure the python file rendering the template is 
#not in the same folder as the template itself, this will not work
#instead put the template in a separate folder and put that separate folder in 
#the same folder as the rendering python file

@app.route("/")
def index():
    return render_template("index.html")