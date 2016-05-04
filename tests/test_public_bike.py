from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'gca'
from tests.test_basic import BasicTestAppium


class PublicBikePageTestAppium(BasicTestAppium):
    def setUp(self):
        super().setUp()
        self.bike_button = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Bicycle")')
        self.bike_button.click()

    def test_vehicles_views_is_scrollable(self):
        wait = WebDriverWait(self.driver, 25)
        wait.until(
            lambda driver: self.driver.find_element_by_android_uiautomator('new UiSelector().text("Vehicles")')
        )
        # self.driver.find_element_by_link_text('WDesk').click()
        self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('new UiSelector().text("Vehicles")'))
        vehicle_elements = self.driver.find_elements_by_xpath('//android.widget.RelativeLayout')
        self.driver.scroll(vehicle_elements[-1],vehicle_elements[0])
        self.driver.scroll(vehicle_elements[0],vehicle_elements[-1])


    # TODO(Red): Needed to be test google map

    # TODO(Red): Needed to be test display options

    def tearDown(self):
        super().tearDown()
