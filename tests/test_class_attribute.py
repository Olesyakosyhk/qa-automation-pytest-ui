import allure

from pages import PlaygroundPage


class TestClassAttribute:
    def test_class_attribute_positive(
            self,
            playground_page: PlaygroundPage,
            go_to_main_page,
    ):
        with allure.step('Переход на страницу "class_attribute"'):
            playground_page.main_page.click_class_attribute_btn()

        with allure.step('Нажать на  голубую кнопку'):
            playground_page.class_attribute.click_blue_btn()

        with allure.step('Принять alert'):
            playground_page.class_attribute.accept_alert()

    def test_class_attribute_url(
            self,
            playground_page: PlaygroundPage,
            go_to_main_page,
    ):
        with allure.step('Переход на страницу "class_attribute"'):
            playground_page.main_page.click_class_attribute_btn()

        with allure.step('Проверка url страницы "class_attribute"'):
            assert playground_page.class_attribute.check_ajax_url()
