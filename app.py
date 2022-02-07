from flask import Flask, redirect, render_template, request, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

from getReviews import *
from analyse import *
from plotGraphs import *

app = Flask(__name__)

#home route
@app.route('/')
def index():
    return render_template('index.html')

#submitting the asin code
@app.route('/submit', methods = ["POST","GET"])
def submit():
    if request.method == "POST":
        asin = request.form["asin"]
        return redirect(url_for("dashboard", asin = asin))
    else:
        return redirect(url_for("error"))

#dashboard route
@app.route("/<asin>")
def dashboard(asin):
    reviews = getreviews(asin)
    clean_reviews = process_reviews(reviews)
    sentiment = sentiment_analysis(clean_reviews)
    opinion = opinion_mine(clean_reviews)

    x = plot_pie(sentiment)
    y = plot_bar(opinion)
    return f"<h1> plots</h1><body> {x, y} </body>"




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
