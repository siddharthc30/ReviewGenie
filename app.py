from flask import Flask, redirect, render_template, request
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
@app.route('/<asin>', methods = ["POST","GET"])
def dashboard(asin):
    asin = request.form.get("asin")

    df = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 
      'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    })
    fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("test.html", graphJSON = graphJSON)
















    

@app.route('/test')
def test():
    return render_template("test2.html")

#Error page route
@app.route('/error')
def error():
    return render_template("error.html")



#strarting the app
if __name__ == "__main__":
    app.run(debug = True)
