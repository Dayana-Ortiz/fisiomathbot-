from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "fisiomathbot_secret_key"

# === Crear BD si no existe ===
def init_db():
    if not os.path.exists("usuarios.db"):
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT UNIQUE NOT NULL,
                contrasena TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

init_db()

# === RUTA PRINCIPAL ===
@app.route("/")
def index():
    if "usuario" in session:
        return render_template("index.html", usuario=session["usuario"])
    else:
        return redirect(url_for("login"))

# === LOGIN ===
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        contrasena = request.form["contrasena"]

        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo=? AND contrasena=?", (correo, contrasena))
        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            session["usuario"] = usuario[1]
            flash(f"Bienvenido, {usuario[1]}!", "success")
            return redirect(url_for("index"))
        else:
            flash("Correo o contraseña incorrectos", "error")

    return render_template("login.html")

# === REGISTRO ===
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        contrasena = request.form["contrasena"]

        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (nombre, correo, contrasena) VALUES (?, ?, ?)",
                           (nombre, correo, contrasena))
            conn.commit()
            flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("El correo ya está registrado.", "error")
        finally:
            conn.close()

    return render_template("register.html")

# === CERRAR SESIÓN ===
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    flash("Has cerrado sesión correctamente.", "info")
    return redirect(url_for("login"))

# === MÓDULOS ===
@app.route("/fisica")
def fisica():
    if "usuario" in session:
        return render_template("fisica.html", usuario=session["usuario"])
    return redirect(url_for("login"))

@app.route("/matematicas")
def matematicas():
    if "usuario" in session:
        return render_template("matematicas.html", usuario=session["usuario"])
    return redirect(url_for("login"))

@app.route("/tecnologia")
def tecnologia():
    if "usuario" in session:
        return render_template("tecnologia.html", usuario=session["usuario"])
    return redirect(url_for("login"))

@app.route("/simulador")
def simulador():
    if "usuario" in session:
        return render_template("simulador.html", usuario=session["usuario"])
    return redirect(url_for("login"))

# === EJECUCIÓN ===
if __name__ == "__main__":
    app.run(debug=True)
