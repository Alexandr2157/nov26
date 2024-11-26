import time
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')


def test_too_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.open()
    homepage.click_monitor()
    time.sleep(3)
    homepage.check_product_count(2)