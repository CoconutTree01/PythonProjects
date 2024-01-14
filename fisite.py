from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

menu = ["Download", "First App", "Feedback"]

@app.route("/")
def index():
    return render_template('index.html',title="Main Page", menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="About Page", menu=menu)

@app.route("/profile/<username>")
def profile(username):
    return f" User: {username} "


with app.test_request_context():
    print((url_for('index')))

if __name__ == "__main__":
   app.run(debug=True)