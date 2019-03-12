from flask import Flask, render_template

app = Flask("Projeto")

@app.route("/")
def ola_mundo():
    return render_template("index.html"), 200

@app.route("/getype")
def go_get():
    return render_template("get.html"), 200

@app.route("/getpost")
def go_post():
    return render_template("post.html"), 200
    
@app.route("/about")
@app.route("/about/<name>")
@app.route("/about/<name>/<age>")
def about(name = None, age = None):
    return "Maciota conhece o {} de {} anos".format(name,age), 200



app.run(debug=True)