from selenium.webdriver.common.by import By



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".page_inner span a.btn-default")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_ITEM_TEXT = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    PRICE_BASKET_ALERT = (By.CSS_SELECTOR, "#messages p:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")

class BasketPageLocators():
    PAY_BUTTON = (By.CSS_SELECTOR, ".clearfix a")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")