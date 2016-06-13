from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'gca'
from tests.test_basic import BasicTestAppium


class NearbyPageTestAppium(BasicTestAppium):
    def setUp(self):
        super().setUp()
        button = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Nearby")')
        button.click()

    def input_place(self):
        wait = WebDriverWait(self.driver, 25)
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

    def test_all_info_is_corrective(self):
        # wait = WebDriverWait(self.driver, 25)
        # wait.until(
        #     lambda driver: self.driver.find_element_by_xpath("//android.widget.TextView[@text='Nearby']")
        # )
        self.input_place()
        stop_name = self.driver.find_elements_by_id('nexti.android.bustaipei:id/text_stopname')
        print(stop_name)

    # TODO(Red): its image is kind of broken, i don't know how to test it.

    def tearDown(self):
        super().tearDown()
