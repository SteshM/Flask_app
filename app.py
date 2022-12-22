from flask import Flask
app = Flask(__name__)

#This is  a small flask app
@app.route("/") #decorator(maps the url route / to the function)
def home():  #function
    return "Hello, Flask!"
