import allure
import pytest

from app.pages import Pages


@allure.parent_suite('REGRESSION')
@allure.suite('VerifyTextPage')
@pytest.mark.regression
@pytest.mark.verify_text_page
class TestVerifyTextPage:

    @allure.title('Тест №11 для страницы "verify_text".')
    @allure.description('Проверка соответствия текста приветствия на странице.')
    def test_verify_text_positive(
            self,
            playground_page: Pages,

    ):
        with allure.step('Переход на страницу "verify_text"'):
            playground_page.verify_text_page.go_to_page_by_url()

        with allure.step('Проверка соответствия текста приветствия на странице'):
            assert playground_page.verify_text_page.target_text.check_text(
                text='Welcome UserName!',
            )
