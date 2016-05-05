from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'gca'
from tests.test_basic import BasicTestAppium


class MRTPageTestAppium(BasicTestAppium):
    def setUp(self):
        super().setUp()
        button = self.driver.find_element_by_android_uiautomator('new UiSelector().text("MRT")')
        button.click()

    def test_all_spinner_correct(self):
        wait = WebDriverWait(self.driver, 25)
        wait.until(
            lambda driver: self.driver.find_element_by_android_uiautomator('new UiSelector().text("MRT Route Map")')
        )
        spinners = self.driver.find_elements_by_xpath('//android.widget.Spinner')
        spinners[0].click()
        display_on_station = self.driver.find_elements_by_xpath('//android.widget.TextView')
        display_on_station[0].click()
        spinners[1].click()
        under_construction = self.driver.find_elements_by_xpath('//android.widget.TextView')
        under_construction[0].click()
        for display_elements in display_on_station:
            spinners[0].click()
            display_elements.click()
            for construct_element in under_construction:
                spinners[1].click()
                construct_element.click()


    # TODO(Red): its image is kind of broken, i don't know how to test it.

    def tearDown(self):
        super().tearDown()
