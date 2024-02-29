from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html", methods=["GET", "POST"])

if __name__ == '__main__':
    app.run(debug=True)