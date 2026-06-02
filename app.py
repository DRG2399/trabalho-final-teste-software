from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.secret_key = "chave-simples-para-trabalho-academico"

VALID_USERNAME = "admin"
VALID_PASSWORD = "123456"


def validate_login(username, password):
    """Valida as credenciais usadas no fluxo de login."""
    if not username or not password:
        return False, "Preencha usuário e senha."

    if username != VALID_USERNAME:
        return False, "Usuário ou senha inválidos."

    if password != VALID_PASSWORD:
        return False, "Usuário ou senha inválidos."

    return True, "Login realizado com sucesso."


def validate_contact(name, email, message):
    """Valida os campos do formulário de contato."""
    if not name:
        return False, "O nome é obrigatório."

    if not email:
        return False, "O email é obrigatório."

    if "@" not in email or "." not in email:
        return False, "Informe um email válido."

    if not message:
        return False, "A mensagem é obrigatória."

    if len(message) < 10:
        return False, "A mensagem deve ter pelo menos 10 caracteres."

    return True, "Mensagem enviada com sucesso."


def login_required():
    """Verifica se existe usuário autenticado na sessão."""
    return session.get("username") == VALID_USERNAME


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        is_valid, message = validate_login(username, password)

        if is_valid:
            session["username"] = username
            return redirect(url_for("dashboard"))

        error = message

    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if not login_required():
        return redirect(url_for("login"))

    return render_template("dashboard.html", username=session["username"])


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if not login_required():
        return redirect(url_for("login"))

    error = None
    success = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        is_valid, response_message = validate_contact(name, email, message)

        if is_valid:
            success = response_message
        else:
            error = response_message

    return render_template("contact.html", error=error, success=success)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
