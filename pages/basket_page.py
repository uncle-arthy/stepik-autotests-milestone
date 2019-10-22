from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_basket_is_empty_message(self):
        basket_is_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT_PARAGRAPH).text

        assert "Your basket is empty." in basket_is_text, "No 'Your basket is empty.' message"
