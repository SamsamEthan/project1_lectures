from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    #defining variable called headline
    headline = "hello, world"

    #   added extra line (headline=headline), passed an additional argument
    #   basically saying in addition to index.html you should also know that i want the variable headline
    #   to be defined in index.html to be whatever headline is equal to (defined above)

        #   effectively i am giving this index.html file knowledge of a new variable

    return render_template("index.html",headline=headline)

@app.route("/bye")
def bye():
    headline = "goodbye"
    return render_template("index.html", headline=headline)

