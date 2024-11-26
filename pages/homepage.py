from selenium.webdriver.common.by import By

class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://demoblaze.com/')

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, '(//a[@href="prod.html?idp_=1"])[2]')
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.XPATH, '''//a[@onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_product_count(self, count):
        monitors = self.driver.find_elements(By.XPATH, '//a[@class="hrefch"]')
        assert len(monitors) == count
