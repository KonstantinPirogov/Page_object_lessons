from pages.product_page import ProductPage
import pytest

#@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ["0","1", "2", "3", "4", "5", "6",  pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.check_basket_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket_without_matan()
    page.no_success_message_on_page()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
    page = ProductPage(browser, link)
    page.open()
    page.no_success_message_on_page()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket_without_matan()
    page.success_message_are_vanish()
