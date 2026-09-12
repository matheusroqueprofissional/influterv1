from flask import Flask, redirect, render_template, url_for
from flask import request

import mysql.connector

from flask import Flask, render_template
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
app = Flask(__name__, template_folder=str(ROOT / "html"))

# Caminho da pasta v01

def conectar_banco():
    return mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="#Luis454049",
    database="users"
    )

@app.route("/register",methods=["GET", "POST"])
def registro():
    conectar_banco()
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        conexao = conectar_banco()
        cursor = conexao.cursor()


        valores = (
            username,
            email,
            password
        )

        sql = """INSERT INTO user (username, email, password) VALUES (%s, %s, %s)"""

        try:
            cursor.execute(sql, valores)
            conexao.commit()

        except mysql.connector.IntegrityError:
            cursor.close()
            conexao.close()

            return "Username ou email já cadastrado."

        cursor.close()
        conexao.close()

        return redirect(url_for("http://localhost:5500/v01/html/", username=username))
    return render_template("http://localhost:5500/v01/html/")



if __name__ == "__main__": 
    app.run(debug=True)
