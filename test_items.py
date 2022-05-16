from selenium.webdriver.common.by import By

from conftest import browser


def test_cart_button_is_visible(browser):
    browser.get(f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    

    cart_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert cart_button.is_enabled(), 'Кнопка добавления в корзину отсутствует'
