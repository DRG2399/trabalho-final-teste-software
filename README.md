# Trabalho Final de Teste de Software

Projeto academico em Python Flask criado para demonstrar testes automatizados de caixa preta e caixa branca.

## Descricao da Aplicacao

A aplicacao possui dois fluxos principais:

- login de usuario;
- envio de formulario de contato.

O sistema usa sessao Flask para controlar o usuario logado. Apenas usuarios autenticados podem acessar o dashboard e o formulario de contato.

## Tecnologias Usadas

- Python
- Flask
- Pytest
- Selenium WebDriver
- WebDriver Manager
- HTML
- CSS

## Usuario e Senha de Teste

- Usuario: `admin`
- Senha: `123456`

## Como Instalar as Dependencias

No terminal, dentro da pasta do projeto, execute:

```bash
pip install -r requirements.txt
```

## Como Executar a Aplicacao

Execute:

```bash
python app.py
```

Depois acesse:

```text
http://127.0.0.1:5000/login
```

## Como Executar os Testes

Para executar todos os testes do projeto:

```bash
python -m pytest
```

Resultado esperado:

```text
16 passed
```

Para executar apenas os testes unitarios:

```bash
python -m pytest tests/test_login_unit.py tests/test_contact_unit.py
```

Para executar apenas os testes Selenium:

```bash
python -m pytest tests/test_selenium.py
```

Os testes Selenium usam Google Chrome em modo headless e o `webdriver-manager` para gerenciar o ChromeDriver.

## Estrutura do Projeto

```text
trabalho-final-teste-software/
|-- app.py
|-- requirements.txt
|-- README.md
|-- templates/
|   |-- login.html
|   |-- dashboard.html
|   `-- contact.html
|-- static/
|   `-- style.css
|-- tests/
|   |-- test_login_unit.py
|   |-- test_contact_unit.py
|   `-- test_selenium.py
`-- docs/
    |-- tabelas_decisao.md
    `-- evidencias/
        `-- README.md
```

## Observacoes Sobre os Testes

Os testes unitarios verificam diretamente as funcoes `validate_login` e `validate_contact`, caracterizando testes de caixa branca.

Os testes Selenium simulam o uso real da aplicacao no navegador, caracterizando testes de caixa preta.
