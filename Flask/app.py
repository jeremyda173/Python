from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Woooorld!'

@app.route('/hello/<string:name>')
def hello(name):
    return f'Hello, {name}!'
    
if __name__ == "__main__":
    app.run(debug=True)