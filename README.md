# Task28.1
<h1 align="center">Итоговый проект по автоматизации тестирования </a> </h1>

Объект тестирования: [Ростелеком IT]( https://b2c.passport.rt.ru/)

[Требования по проекту](https://docs.yandex.ru/docs/view?url=ya-browser%3A%2F%2F4DT1uXEPRrJRXlUFoewruO2sT530Vvqy8MXx3BMRR5WPDV_X5_YBtnmvIPr55hOXU7pC69d52kQkNxmDSg8cXnhEooHUFte9E60PA2EWJLSdTV-VY5OljIREQKTlzXx06UdD-RF5UKiQH91z1_Q9UQ%3D%3D%3Fsign%3DqKHpxpZvAf5X9APwBAkwUOPqICBYA4bstZeWJ6teiGM%3D&name=Требования_SSO_для_тестирования_last.doc&nosw=1)

  Техническое задание:
1. Протестировать требования.
2. Разработать тест-кейсы (не менее 20). Необходимо применить несколько техник тест-дизайна.
3. Провести автоматизированное тестирование продукта (не менее 20 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс. Оформите свой набор автотестов в GitHub.
4. Оформить описание обнаруженных дефектов. Во время обучения вы работали с разными сервисами и шаблонами, используйте их для оформления тест-кейсов и обнаруженных дефектов. (если дефекты не будут обнаружены, то составить описание трех дефектов)

  В рамках проекта произведено ручное и автоматизированное тестирование нового интерфейса авторизации в личном кабинете по паттерну PageObject с применением библиотек PyTest и Selenium Webdriver. Тесты проверяют авторизацию и восстановление пароля в личном кабинете

  Сформированы [тест-кейсы и отчёты о дефектах](https://docs.google.com/spreadsheets/d/10aG4ToZBRYa0f-dH_O-Ab4_E6uBeFuK8sgdiqJle0rU/edit?usp=sharing)
  
Для разработки тест-кейсов использованы методы:
- "Черный ящик"
- функционального тестирование
- UX тестирование.
Так же использованы техники тест дизайна:
- разбиение на классы эквивалентности
- анализ граничных значений
- тестирование состояний и переходов

<h1 align=>Структура проекта:</h1>

**README.md - содержит информацию о проекте.**

**conftest.py - описание фикстур для проекта.**

**requirements.txt - список внешних зависимостей.**

**Директория chromedriver_win32 содержит:**

 - chromedriver.exe -Драйвер для управления браузером Chrome


**Директория pages содержит:**

- base_page.py - описание атрибутов и методов работы с базовой страницей.

- auth_page.py - описание атрибутов и методов работы со страницей авторизации проекта.

- reset_page.py - описание атрибутов и методов работы со страницей восстановления пароля проекта.

- locators.py - описание локаторов проекта.


**Директория tests содержит:**

- test_auth_page.py - тесты страницы авторизации проекта.

- test_reset_page.py - тесты страницы восстановления пароля проекта.

- config.py - описание значений элементов страниц и переменных.

Тесты настроены на запуск через "Run"

Окружение: Windows 11 Версия 21H2

Браузер: Google Chrome 112.0.5615.138 (64-bit)
