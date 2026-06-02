from app import validate_contact


def test_contato_valido():
    is_valid, message = validate_contact(
        "Daniel",
        "daniel@email.com",
        "Mensagem válida para contato.",
    )

    assert is_valid is True
    assert message == "Mensagem enviada com sucesso."


def test_contato_com_nome_vazio():
    is_valid, message = validate_contact("", "daniel@email.com", "Mensagem válida.")

    assert is_valid is False
    assert message == "O nome é obrigatório."


def test_contato_com_email_vazio():
    is_valid, message = validate_contact("Daniel", "", "Mensagem válida.")

    assert is_valid is False
    assert message == "O email é obrigatório."


def test_contato_com_email_invalido():
    is_valid, message = validate_contact("Daniel", "daniel-email", "Mensagem válida.")

    assert is_valid is False
    assert message == "Informe um email válido."


def test_contato_com_mensagem_vazia():
    is_valid, message = validate_contact("Daniel", "daniel@email.com", "")

    assert is_valid is False
    assert message == "A mensagem é obrigatória."


def test_contato_com_mensagem_curta():
    is_valid, message = validate_contact("Daniel", "daniel@email.com", "Oi")

    assert is_valid is False
    assert message == "A mensagem deve ter pelo menos 10 caracteres."
