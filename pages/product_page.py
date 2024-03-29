from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_infoboxes(self):
        self.should_be_product_added_to_basket_box()
        self.should_be_same_title_in_success_box_and_in_description()
        self.should_be_total_basket_price_box()
        self.should_be_same_total_basket_price_and_product_price()

    def should_be_product_added_to_basket_box(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_BOX), \
            "No 'Successfully Add to basket' messagebox"

    def should_be_same_title_in_success_box_and_in_description(self):
        product_name_in_messagebox = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_BOX).text
        product_name_in_description = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_DESCRIPTION).text

        assert product_name_in_description == product_name_in_messagebox, "Product names in messagebox and" \
                                                                          "in description doesn't match"

    def should_be_total_basket_price_box(self):
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE_IN_BASKET_BOX), \
            "No 'Total price in a basket' messagebox"

    def should_be_same_total_basket_price_and_product_price(self):
        price_in_messagebox = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_IN_BOX).text
        price_in_description = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_DESCRIPTION).text

        assert price_in_description == price_in_messagebox, "Prices in messagebox and " \
                                                            "in description doesn't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_BOX), \
            "Success message is presented, but should not be"

    def should_be_dissapearing_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_BOX), \
            "Success message is still presented, but should dissapear"
