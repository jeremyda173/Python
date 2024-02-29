from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tareas = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/add")
def add():
    if request.method == 'GET':
        return render_template("add.html", methods=["GET", "POST"])
    else:
        tarea = request.form['task']
        tareas.append(tarea)
        return redirect("/home")
    
if __name__ == '__main__':
    app.run(debug=True)