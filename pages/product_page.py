from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_item_to_basket(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        add_item = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_item.click()
        self.solve_quiz_and_get_code()
        message_text = self.browser.find_element(*ProductPageLocators.ADD_ITEM_TEXT).text
        basket_text = self.browser.find_element(*ProductPageLocators.PRICE_BASKET_ALERT).text
        assert item_name in message_text, f"ожидаю '{item_name}'  - подстрока '{message_text}'"
        assert item_price in basket_text, f"ожидаю '{item_price}'  - подстрока '{basket_text}'"