import pytest
import time
from pages.auth_page import AuthPage, GlobalLocators
from pages.locators import AuthLocators
from tests.config import Config


@pytest.mark.auth
def test_check_elem_auth_form(chrome_browser):
    """Тест TC-002 Проверка формы "Авторизация" """
    page = AuthPage(chrome_browser)
    assert page.get_right_elem_auth() == Config.REQ_ELEMENTS_AUTH

@pytest.mark.auth
def test_default_login(chrome_browser):
    """Тест TC-003, Проверка форм "Авторизации" по умолчанию выбрана форма авторизации по телефону """
    page = AuthPage(chrome_browser)
    assert page.get_text_from_login() == Config.DEFAULT_LOGIN_TEXT

@pytest.mark.auth
def test_cheсk_about_slogan(chrome_browser):
    """ Тест TC-004 Проверка наличия на странице авторизации продуктового слогана ЛК "Ростелеком ID" """
    page = AuthPage(chrome_browser)
    assert page.check_info_about_slogan() == Config.TAGLINE_TEXT

@pytest.mark.auth
def test_chek_info_for_users(chrome_browser):
    """Тест TC-005 Проверка наличия вспомогательной информации для клиента в левой части страницы авторизации"""
    page = AuthPage(chrome_browser)
    assert "Пользовательское соглашение" in page.find_element(GlobalLocators.LEFT_BLOCK).text.split('\n'), \
        "В левой части страницы отсутствует вспомогательная информация для клиентов"

def test_active_tab_1(chrome_browser):
    """Тест TC-006 Проверка автоматического переключения табa c номера телефона на почту"""
    page = AuthPage(chrome_browser)
    page.enter_login(Config.VALID_EMAIL)
    page.enter_pass(Config.VALID_PASSWORD)
    assert page.find_element(AuthLocators.AUTH_placeholder).text == 'Электронная почта'


def test_active_tab_2(chrome_browser):
    """Тест TC-007 Проверка автоматического переключения таба с почты на телефон"""
    page = AuthPage(chrome_browser)
    page.click_email_tab()
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)
    assert page.find_element(AuthLocators.AUTH_placeholder).text == 'Мобильный телефон'

def test_active_tab_3(chrome_browser):
    """Тест TC-008 Проверка автоматического переключения таба с логина на телефон"""
    page = AuthPage(chrome_browser)
    page.click_login_tab()
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)
    time.sleep(5)
    print(AuthLocators.TAB_TEL)
    assert page.find_element(AuthLocators.AUTH_placeholder).text == 'Мобильный телефон'

def test_active_tab_4(chrome_browser):
    """Тест TC-009 Проверка автоматического переключения таба с ЛС на телефон"""
    page = AuthPage(chrome_browser)
    page.click_LS_tab()
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)
    time.sleep(2)
    assert page.find_element(AuthLocators.AUTH_placeholder).text == 'Мобильный телефон'

def test_active_tab_5(chrome_browser):
    """Тест TC-010 Проверка автоматического переключения таба с логина на почту"""
    page = AuthPage(chrome_browser)
    page.click_login_tab()
    page.enter_login(Config.VALID_EMAIL)
    page.enter_pass(Config.VALID_PASSWORD)
    assert page.find_element(AuthLocators.AUTH_placeholder).text == 'Электронная почта'

def test_login_with_valid_phone(chrome_browser):
    """Тест TC-011 Проверка авторизации по кнопке "Номер" с валидными данными """
    page = AuthPage(chrome_browser)
    page.find_captcha()
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)
    page.btn_click()
    page.find_logout_btn()
    assert page.get_relative_link() == '/account_b2c/page', "Пользователь не авторизован"
    page.logout_btn_click()

def test_login_with_invalid_phone(chrome_browser):
    """Тест TC-012 Проверка авторизации по кнопке "Номер" с невалидными данными номера """
    page = AuthPage(chrome_browser)
    page.enter_login(Config.INVALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)
    time.sleep(25) #Время для введения капчи вручную
    page.btn_click()
    error_mess = page.find_element(AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'

@pytest.mark.auth
def test_login_with_valid_email(chrome_browser):
    """Тест TC-013 Проверка авторизация по кнопке "Почта" с валидными данными почты """
    page = AuthPage(chrome_browser)
    page.find_captcha()
    page.click_email_tab()
    page.enter_login(Config.VALID_EMAIL)
    page.enter_pass(Config.VALID_PASSWORD)
    page.btn_click()
    page.find_logout_btn()
    assert page.get_relative_link() == '/account_b2c/page', "Пользователь не авторизован"
    page.logout_btn_click()

@pytest.mark.auth
def test_login_with_invalid_email(chrome_browser):
    """Тест TC-014 Проверка авторизация по кнопке "Почта" с невалидными данными почты"""
    page = AuthPage(chrome_browser)
    page.click_email_tab()
    page.enter_login(Config.INVALID_EMAIL)
    page.enter_pass(Config.VALID_PASSWORD)
    time.sleep(25)  # Время для введения капчи вручную
    page.btn_click()
    error_mess = page.find_element(AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'

def test_login_with_valid_phone_invalid_pass(chrome_browser):
    """Тест TC-015 Проверка авторизации по кнопке "Номер" с невалидным паролем """
    page = AuthPage(chrome_browser)
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.INVALID_PASSWORD)
    time.sleep(10) #Время для введения капчи вручную
    page.btn_click()
    error_mess = page.find_element(AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'

def test_login_with_valid_email_invalid_pass(chrome_browser):
    """Тест TC-016 Проверка авторизации по кнопке "Номер" с невалидным паролем """
    page = AuthPage(chrome_browser)
    page.click_email_tab()
    page.enter_login(Config.VALID_EMAIL)
    page.enter_pass(Config.INVALID_PASSWORD)
    time.sleep(25)  # Время для введения капчи вручную
    page.btn_click()
    error_mess = page.find_element(AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'

