from flask import Flask, render_template

app = Flask("Projeto")

@app.route("/")
def ola_mundo():
    return "Oi, meu chapa", 200

app.run()