from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

menu = ["Download", "First App", "Feedback"]

@app.route("/")
def index():
    return render_template('index.html',title="Main Page", menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="About Page", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)