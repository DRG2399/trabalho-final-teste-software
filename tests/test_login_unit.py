from app import validate_login


def test_login_correto():
    is_valid, message = validate_login("admin", "123456")

    assert is_valid is True
    assert message == "Login realizado com sucesso."


def test_login_com_senha_errada():
    is_valid, message = validate_login("admin", "senha_errada")

    assert is_valid is False
    assert message == "Usuário ou senha inválidos."


def test_login_com_usuario_inexistente():
    is_valid, message = validate_login("aluno", "123456")

    assert is_valid is False
    assert message == "Usuário ou senha inválidos."


def test_login_com_campos_vazios():
    is_valid, message = validate_login("", "")

    assert is_valid is False
    assert message == "Preencha usuário e senha."
