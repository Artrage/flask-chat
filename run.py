import os
from flask import flask

app = Flask(_name_)

@app.route('/')
def index():
    return "<h1>Hello there</h1>"

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)