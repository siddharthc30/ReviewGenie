from flask import Flask, redirect, render_template, request, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

#home route
@app.route('/')
def index():
    return render_template('index.html')

#Dashboard of results route
@app.route('/submit', methods = ["POST","GET"])
def submit():
    if request.method == "POST":
        asin = request.form["asin"]
        return redirect(url_for("dashboard", asin = asin))
    else:
        return redirect(url_for("error"))

@app.route("/<asin>")
def dashboard(asin):
    return f"<h1> {asin} </h1>"




# @app.route('/test')
# def test():
#     return render_template("test2.html")

#Error page route
@app.route('/error')
def error():
    return render_template("error.html")



#strarting the app
if __name__ == "__main__":
    app.run(debug = True)
