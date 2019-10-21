from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADD_TO_CART_SUCCESS_BOX = (By.CSS_SELECTOR, "div.alertinner")
    TOTAL_PRICE_IN_CART_BOX = (By.CSS_SELECTOR, ".alert-info div.alertinner")

    PRODUCT_NAME_IN_SUCCESS_BOX = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME_IN_DESCRIPTION = (By.CSS_SELECTOR, ".product_main h1")

    TOTAL_PRICE_IN_BOX = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRODUCT_PRICE_IN_DESCRIPTION = (By.CSS_SELECTOR, ".product_main .price_color")
