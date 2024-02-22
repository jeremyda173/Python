from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Yarisa"
    return render_template('index.html', name=name)

@app.route('/hello/<string:name>')
def hello(name):
    return f'Hello, {name}!'
    
if __name__ == "__main__":
    app.run(debug=True)