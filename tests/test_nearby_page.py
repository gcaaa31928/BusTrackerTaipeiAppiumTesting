from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'gca'
from tests.test_basic import BasicTestAppium


class NearbyPageTestAppium(BasicTestAppium):
    def setUp(self):
        super().setUp()
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(
            lambda driver: self.driver.find_element_by_android_uiautomator('new UiSelector().text("Nearby")')
        )
        button.click()

    def input_place(self):
        wait = WebDriverWait(self.driver, 15)
        input = wait.until(
            lambda driver: self.driver.find_element_by_id("nexti.android.bustaipei:id/text_place")
        )
        input.click()
        input_place = wait.until(
            lambda driver: self.driver.find_element_by_id("nexti.android.bustaipei:id/edit_place")
        )
        input_place.send_keys('no. 8, section 3, civic blvd')
        self.driver.find_element_by_id('nexti.android.bustaipei:id/button_go').click()
        first_place = wait.until(
            lambda driver: self.driver.find_element_by_xpath("//android.widget.TextView[@index='0' and @resource-id='nexti.android.bustaipei:id/text_name']")
        )
        first_place.click()

    def click_first_stop(self):
        self.input_place()
        wait = WebDriverWait(self.driver, 15)
        stop = wait.until(
            lambda driver: self.driver.find_element_by_id('nexti.android.bustaipei:id/text_stopname')
        )
        stop.click()

    def tearDown(self):
        super().tearDown()
