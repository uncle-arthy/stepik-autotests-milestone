from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTRATION_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FORM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_FORM_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_FORM_REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADD_TO_BASKET_SUCCESS_BOX = (By.CSS_SELECTOR, "div.alertinner")
    TOTAL_PRICE_IN_BASKET_BOX = (By.CSS_SELECTOR, ".alert-info div.alertinner")

    PRODUCT_NAME_IN_SUCCESS_BOX = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME_IN_DESCRIPTION = (By.CSS_SELECTOR, ".product_main h1")

    TOTAL_PRICE_IN_BOX = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRODUCT_PRICE_IN_DESCRIPTION = (By.CSS_SELECTOR, ".product_main .price_color")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BASKET_TEXT_PARAGRAPH = (By.CSS_SELECTOR, "#content_inner p")
