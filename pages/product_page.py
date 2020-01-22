from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_item_to_basket(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        add_item = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_item.click()
        self.solve_quiz_and_get_code()
        item_name_string = f"{item_name} has been added to your basket."
        message_text = self.browser.find_element(*ProductPageLocators.ADD_ITEM_TEXT).text
        assert item_name_string in message_text, f"ожидаю '{item_name_string}' - строка '{message_text}'"

    def add_item_to_basket_without_matan(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        add_item = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_item.click()
        item_name_string = f"{item_name} has been added to your basket."
        message_text = self.browser.find_element(*ProductPageLocators.ADD_ITEM_TEXT).text
        assert item_name_string in message_text, f"ожидаю '{item_name_string}' - строка '{message_text}'"

    def check_basket_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_price_text = self.browser.find_element(*ProductPageLocators.PRICE_BASKET_ALERT).text
        assert item_price in basket_price_text, f"ожидаю '{item_price}'  - подстрока '{basket_price_text}'"

    def no_success_message_on_page(self):
        # проверяем, что при переходе на страницу нет успешного добавления в корзину
        assert self.is_not_element_present(*ProductPageLocators.ADD_ITEM_TEXT), "Элемент появился!!!"

    def success_message_are_vanish(self):
        # проверяем, что сообщение о добавлении исчезает
        assert self.is_not_element_present(*ProductPageLocators.ADD_ITEM_TEXT), "Элемент не исчез!!!"
