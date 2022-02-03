from flask import Flask, redirect, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<asin>', methods = ["POST","GET"])
def dashboard(asin):
    asin = request.form.get("asin")

    return render_template("test.html", asin = asin)


if __name__ == "__main__":
    app.run(debug = True)
