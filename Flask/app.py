from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

# create 3 routes age, name, and favorite_food, class and return strings for them

@app.route("/age")
def age() : 
    return '19' 

@app.route("/name")
def name(): 
    return "Yagyesh"

@app.route("/section")
def section(): 
    return "B4"