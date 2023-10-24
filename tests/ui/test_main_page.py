import allure
from allure_commons.types import Severity

from demoblaze_test_project.pages.index import Index

index = Index()


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('UI')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем лейбл в шапке сайта')
def test_label():
    index.open_main_page()

    index.should_label_be_clickable_and_have_text()


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('UI')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем панель навигации')
def test_header():
    index.open_main_page()

    index.should_be_navbar_example()


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('UI')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем заголовок блока CATEGORIES')
def test_categories():
    index.open_main_page()

    index.should_categories_be_clickable()


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('UI')
@allure.severity(Severity.CRITICAL)
@allure.title('Проверяем фильтрацию по телефонам')
def test_phones_filter():
    index.open_main_page()

    index.click_phones()

    index.should_have_gadget('Samsung galaxy s6')


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('UI')
@allure.severity(Severity.CRITICAL)
@allure.title('Проверяем фильтрацию по лэптопам')
def test_laptops_filter():
    index.open_main_page()

    index.click_laptops()

    index.should_have_gadget('MacBook air')


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('UI')
@allure.severity(Severity.CRITICAL)
@allure.title('Проверяем фильтрацию по мониторам')
def test_monitors_filter():
    index.open_main_page()

    index.click_monitors()

    index.should_have_gadget('Apple monitor 24')


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('UI')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем подвал сайта')
def test_footer():
    index.open_main_page()

    index.should_footer_have_text()
