import threading
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from werkzeug.serving import make_server

from app import app


BASE_URL = "http://127.0.0.1:5000"


class ServerThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.server = make_server("127.0.0.1", 5000, app)
        self.context = app.app_context()
        self.context.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()


@pytest.fixture(scope="session")
def live_server():
    server = ServerThread()
    server.start()
    time.sleep(1)
    yield
    server.shutdown()


@pytest.fixture
def browser(live_server):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,768")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    yield driver
    driver.quit()


def login(browser, username="admin", password="123456"):
    browser.get(f"{BASE_URL}/login")
    browser.find_element(By.ID, "username").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()


def test_acessar_pagina_de_login(browser):
    browser.get(f"{BASE_URL}/login")

    assert "Login" in browser.title
    assert browser.find_element(By.TAG_NAME, "h1").text == "Login"


def test_fazer_login_com_dados_corretos(browser):
    login(browser)

    WebDriverWait(browser, 5).until(EC.url_contains("/dashboard"))
    assert "Bem-vindo, admin!" in browser.page_source


def test_tentar_login_com_dados_incorretos(browser):
    login(browser, "admin", "senha_errada")

    error = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "login-error"))
    )
    assert error.text == "Usuário ou senha inválidos."


def test_acessar_formulario_de_contato_apos_login(browser):
    login(browser)
    WebDriverWait(browser, 5).until(EC.url_contains("/dashboard"))
    browser.find_element(By.ID, "contact-link").click()

    WebDriverWait(browser, 5).until(EC.url_contains("/contact"))
    assert browser.find_element(By.TAG_NAME, "h1").text == "Contato"


def test_enviar_formulario_de_contato_valido(browser):
    login(browser)
    WebDriverWait(browser, 5).until(EC.url_contains("/dashboard"))
    browser.get(f"{BASE_URL}/contact")

    browser.find_element(By.ID, "name").send_keys("Daniel")
    browser.find_element(By.ID, "email").send_keys("daniel@email.com")
    browser.find_element(By.ID, "message").send_keys("Mensagem válida para contato.")

    browser.find_element(By.ID, "message").submit()

    success = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "contact-success"))
    )

    assert success.text == "Mensagem enviada com sucesso."


def test_enviar_formulario_de_contato_invalido(browser):
    login(browser)
    WebDriverWait(browser, 5).until(EC.url_contains("/dashboard"))
    browser.get(f"{BASE_URL}/contact")

    browser.find_element(By.ID, "name").send_keys("Daniel")
    browser.find_element(By.ID, "email").send_keys("email-invalido")
    browser.find_element(By.ID, "message").send_keys("Mensagem curta")

    browser.find_element(By.ID, "message").submit()

    error = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "contact-error"))
    )

    assert error.text == "Informe um email válido."
