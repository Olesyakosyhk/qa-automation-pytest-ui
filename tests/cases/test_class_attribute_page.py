import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('ClassAttributePage')
@pytest.mark.regression
@pytest.mark.class_attribute_page
class TestClassAttributePage:

    @allure.title('Тест №2 для страницы "class_attribute".')
    @allure.description('Поиск основной кнопки, с последующим принятием alert')
    def test_class_attribute_positive(
            self,
            playground_page: Pages,
            go_to_class_attribute_page,
    ):
        with allure.step('Нажать на синюю кнопку'):
            playground_page.class_attribute_page.blue_button.click()

        with allure.step('Принять alert'):
            playground_page.class_attribute_page.accept_alert()

    @allure.title('Тест №2.2 для страницы "class_attribute".')
    @allure.description('Проверка url страницы "class_attribute"')
    def test_class_attribute_valid_url(
            self,
            playground_page: Pages,
            go_to_class_attribute_page,
    ):
        with allure.step('Проверка url страницы "class_attribute"'):
            assert playground_page.class_attribute_page.class_attr_page_url.check_url()

    @allure.title('Тест №2.3 для страницы "class_attribute".')
    @allure.description('Проверка присутствия всех кнопок страницы "class_attribute"')
    def test_class_attribute_presents_btn(
            self,
            playground_page: Pages,
            go_to_class_attribute_page,
    ):
        with allure.step('Проверка присутствия всех кнопок страницы "class_attribute"'):
            assert playground_page.class_attribute_page.blue_button.find_and_wait_element()
            assert playground_page.class_attribute_page.yellow_button.find_and_wait_element()
            assert playground_page.class_attribute_page.green_button.find_and_wait_element()

    @allure.title('Тест №2.4 для страницы "class_attribute".')
    @allure.description('Проверка активности всех кнопок страницы "class_attribute"')
    def test_class_attribute_clickable_btn(
            self,
            playground_page: Pages,
            go_to_class_attribute_page,
    ):
        with allure.step('Проверка активности всех кнопок страницы "class_attribute"'):
            assert playground_page.class_attribute_page.blue_button.is_clickable()
            assert playground_page.class_attribute_page.yellow_button.is_clickable()
            assert playground_page.class_attribute_page.green_button.is_clickable()
