from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    # проверяем отсутствие кнопки оплаты
    def check_pay_button_absence(self):
        assert self.is_not_element_present(*BasketPageLocators.PAY_BUTTON), "Кнопка оплаты найдена"

    def check_empty_message_in_basket(self):
        empty_message_string = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        # проверяем наличие строки
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Сообщение о пустой корзине не найдено"
        # проверяем текст
        message_text = "Your basket is empty"
        assert message_text in empty_message_string, f"Ожидаю, что '{message_text}' является подстрокой '{empty_message_string}'"
