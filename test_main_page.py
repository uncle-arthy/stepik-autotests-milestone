from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    main_page.open()                      # открываем страницу
    main_page.should_be_login_link()      # проверяем наличие ссылки авторизации
    main_page.go_to_login_page()          # переходим на страницу авторизации

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()     # проверяем наличие элементов и адрес страницы авторизации
