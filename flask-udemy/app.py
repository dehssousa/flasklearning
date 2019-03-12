from flask import Flask, render_template

app = Flask("Projeto")

@app.route("/")
def ola_mundo():
    return render_template("index.html", meu_nome="Texugo"), 200

app.run(debug=True)
