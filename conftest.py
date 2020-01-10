import pytest
from selenium import webdriver
import chromedriver_binary  #костыль для pycharm
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, fr, etc.")
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

# фикстура для открытия и закрытия браузера с выбором языка
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        user_language = request.config.getoption("language")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        browser = webdriver.Chrome()
        print("\nstart chrome browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()