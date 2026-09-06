from flask import Flask, render_template
from flask import request

import mysql.connector

from flask import Flask, render_template
from pathlib import Path

# Caminho da pasta v01
ROOT = Path(__file__).resolve().parents[2]

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="#Luis454049",
    database="users"
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM user")

resultados = cursor.fetchall()

for usuario in resultados:
    print(usuario)

cursor.close()
conexao.close()


app = Flask(__name__, template_folder=str(ROOT / "html"))

@app.route("/")
def test():
    print("working")
    return "<p>is working</p>"

@app.route("/profile/<username>")
def profile(username):
    return render_template('../html/profile.html',username="matheus")

if __name__ == "__main__": 
    app.run(debug=True)
