import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language')

@pytest.fixture
def browser(request):
    language = request.config.getoption('--language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.maximize_window()
    yield browser
    browser.quit()


