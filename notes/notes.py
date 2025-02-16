#Note taking application example
#This will be able to store different types of notes that the user may take

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

#Defined notes variable, empty list of notes that is eventually going to contain
# the notes that the user will be taking
notes = []

@app.route("/", methods = ["GET","POST"])
def index():
    '''session["notes"] = []'''
    '''if session.get("notes") is None:
        session["notes"] = []'''

    #If the request method is post then access/add a note
    if request.method == "POST":
        note = request.form.get("note")
        '''session["notes"].append(note)'''
        notes.append(note) #take the original empty notes variable and add the new notes

    #Then whether notes are added or not, return the list of notes to the page
    return render_template("index.html",notes=notes)