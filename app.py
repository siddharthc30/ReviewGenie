from flask import Flask, redirect, render_template, request, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

from getData import *
from analyse import *
from plotGraphs import *

app = Flask(__name__)

#home route
@app.route('/')
@app.route('/home')
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
    data = getdata(asin)
    if not data:
        return redirect(url_for("error"))
    else:
        clean_reviews = process_reviews(data['Reviews'])
        sentiment = sentiment_analysis(clean_reviews)
        opinion = opinion_mine(clean_reviews)

        x = plot_pie(sentiment)
        y = plot_bar(opinion)
        return render_template("dashboard.html", pieplot = x, barplot = y, title = data['Product_name'], image_url = data['Image'], rating = data['Rating'])

    
#Error page route
@app.route('/error')
def error():
    return render_template("error.html")

#fix page route
@app.route('/fixing')
def page_fix():
    return render_template("fixing.html")


#strarting the app
if __name__ == "__main__":
    app.run(debug = True)
