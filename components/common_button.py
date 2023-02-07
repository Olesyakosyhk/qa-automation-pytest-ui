from selenium.webdriver.common.by import By

from components.button import Button


class BlueButton(Button):
    LOCATOR_TYPE = By.CSS_SELECTOR
    LOCATOR_PATH = '[class*="btn-primary"]'


class GreenButton(Button):
    LOCATOR_TYPE = By.CSS_SELECTOR
    LOCATOR_PATH = '[class*="btn-success"]'


class YellowButton(Button):
    LOCATOR_TYPE = By.CSS_SELECTOR
    LOCATOR_PATH = '[class*="btn-warning"]'


class RedButton(Button):
    LOCATOR_TYPE = By.CSS_SELECTOR
    LOCATOR_PATH = '[class*="btn-danger"]'
