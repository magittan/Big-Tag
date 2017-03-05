from flask import Flask
from flask import render_template
from operator import itemgetter
from flask import request
import json


app = Flask("The Big Tag")

@app.route("/")


def home():
	return render_template("The Big Tag Front End.html")

if __name__ == "__main__":
	app.run(debug=True)
