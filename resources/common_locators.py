from selenium.webdriver.common.by import By


class CommonLocators:
    BLUE_BTN = (By.CSS_SELECTOR, '[class*="btn-primary"]')
    GREEN_BTN = (By.CSS_SELECTOR, '[class*="btn-success"]')
    YELLOW_BTN = (By.CSS_SELECTOR, '[class*="btn-warning"]')
