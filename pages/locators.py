from selenium.webdriver.common.by import By


class GlobalLocators:
    RIGHT_BLOCK = (By.ID, "page-right")  # правый блок страницы
    LEFT_BLOCK = (By.ID, "page-left")  # левый блок страницы
    TAGLINE = (By.CSS_SELECTOR, ".what-is__desc") #слоган Ростелекома

class AuthLocators:
    AUTH_TITLE = (By.XPATH, "//h1[@class='card-container__title']")  # названия формы "Авторизация"/"Регистрация"/"Восстановить пароль"
    AUTH_BLOCK = (By.CLASS_NAME, "rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs")
    AUTH_placeholder = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    TAB_TEL = (By.ID, "t-btn-tab-phone")  # Таб авторизации по телефону
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")  # Таб авторизации по почте
    TAB_LOGIN = (By.ID, "t-btn-tab-login")  # Таб авторизации по логину
    TAB_LS = (By.ID, "t-btn-tab-ls")  # Таб авторизации по лицевому счету
    AUTH_LOGIN = (By.ID, "username")  # Поле ввода телефона/почты/логина/лицевого счета
    AUTH_PASS = (By.ID, "password")  # Поле ввода пароля
    AUTH_BTN = (By.ID, "kc-login")  # Кнопка "Войти"
    # Текст внутри поля для ввода телефона/почты/логина/лицевого счета
    AUTH_LOGIN_TEXT = (By.XPATH, '//div[@class="rt-input-container tabs-input-container__login"]'
                                 '//span[@class="rt-input__placeholder"]')
    LOGOUT_BTN = (By.ID, "logout-btn")  # Кнопка "Выйти" в личном кабинете
    AUTH_FORM_ERROR = (By.XPATH, "//span[@id='form-error-message']")
    FORGOT_PASSWORD = (By.ID, "forgot_password")

class ResetLocators:
    # Текст из формы восстановления пароля
    TEXT_RESET_FORM = (By.XPATH, "//h1[@class='card-container__title']")
    # Получили id блока, где находится форма авторизации
    RIGHT_BLOCK_TABS = (By.XPATH, '//div[@class="rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs"]')
    AUTH_LOGIN = (By.ID, "username")  # Поле ввода телефона/почты/логина/лицевого счета
    RESET_LOGIN_TEXT = (By.XPATH, ' //*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    CAPTCHA = (By.ID, "captcha")
    BACK_BTN = (By.ID, "reset-back")
    CONTINUE_BTN = (By.ID, "reset-back")
    LOGIN_ERROR_BOX = (By.XPATH, "//*[@class='rt-input-container__meta rt-input-container__meta--error']")
    GENERAL_ERROR_BOX = (By.ID, "form-error-message") #Неверный логин или текст с картинки
    TAB_TEL = (By.ID, "t-btn-tab-phone")  # Таб авторизации по телефону
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")  # Таб авторизации по почте
    TAB_LOGIN = (By.ID, "t-btn-tab-login")  # Таб авторизации по логину
    TAB_LS = (By.ID, "t-btn-tab-ls")  # Таб авторизации по лицевому счету