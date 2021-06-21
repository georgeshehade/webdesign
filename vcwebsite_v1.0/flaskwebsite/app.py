from flask import Flask, render_template
app = Flask(__name__)
import os
cwd = os.getcwd()

@app.route("/")
# @app.route("/home")
def home():
    return render_template("Homepage.html")

@app.route("/explore")
def explore():
    return render_template("Explore.html")

@app.route("/results")
def results():
    return render_template("Results.html")

@app.route("/about")
def about():
    return "<h1>about Page!</h1>"

if __name__ == "__main__":
    app.run(debug=True)