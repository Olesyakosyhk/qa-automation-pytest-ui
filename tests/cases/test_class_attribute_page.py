import allure

from pages import Pages


class TestClassAttributePage:
    def test_class_attribute_positive(
            self,
            playground_page: Pages,
            go_to_class_attribute_page,
    ):
        with allure.step('Нажать на синюю кнопку'):
            playground_page.class_attribute_page.click_blue_btn()

        with allure.step('Принять alert'):
            playground_page.class_attribute_page.accept_alert()

    def test_class_attribute_valid_url(
            self,
            playground_page: Pages,
            go_to_class_attribute_page,
    ):
        with allure.step('Проверка url страницы "class_attribute"'):
            assert playground_page.class_attribute_page.check_url()

    def test_class_attribute_presents_btn(
            self,
            playground_page: Pages,
            go_to_class_attribute_page,
    ):
        with allure.step('Проверка url страницы "class_attribute"'):
            assert playground_page.class_attribute_page.check_presents_btn()

    def test_class_attribute_clickable_btn(
            self,
            playground_page: Pages,
            go_to_class_attribute_page,
    ):
        with allure.step('Проверка url страницы "class_attribute"'):
            assert playground_page.class_attribute_page.check_btn_is_clickable_elements()
