from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    num = [1,2,3,4,5,6,7,8,9,10,11,12]
    return render_template('index.html', num=num)

@app.route('/RedesSociales')
def redes():
    redes = ["Facebook", "Twitter", "Instagram"]
    return render_template('redes.html', redes=redes)


# @app.route('/hello/<string:name>')
# def hello(name):
#     return f'Hello, {name}!'
    
if __name__ == "__main__":
    app.run(debug=True)