from flask import Flask

app = Flask(__name__) #Decorator

@app.route("/")
def index(): #all this index function is doing is telling it to return hello world
    return "Hello world"

#another route named "/david"
#this route when added to the end of the URL, will link to a new HTTP page
@app.route("/david")
def david():
    return "hello im david"

### TEMPLATE ###

#this is not a paritcular route, but a template for a whole generalized set of routes
#basically when the name is passed in via the URL it will activate the function below
#allowing the program to say hello, (name)
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>hello, {name}!<h1>"