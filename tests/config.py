class Config:
    BASE_URL = 'https://b2c.passport.rt.ru/' #страница авторизации
    BASE_REG_URL = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'

    VALID_EMAIL = "Cheklawas@gmail.com"
    VALID_PHONE = "+79209618214"
    INVALID_PHONE = "+72345678987"
    VALID_PASSWORD = "6SA-ypu-xj8-mX2"
    INVALID_EMAIL = "Chek@mail.ru"
    INVALID_PASSWORD = "123456"
    REQ_ELEMENTS_AUTH = ["Авторизация", "Телефон", "Почта", "Логин", "Лицевой счёт"]
    REQ_ELEMENTS_RESET = ["Телефон", "Почта", "Логин", "Лицевой счёт"]
    DEFAULT_LOGIN_TEXT = "Мобильный телефон"
    TAGLINE_TEXT = "Персональный помощник в цифровом мире Ростелекома"