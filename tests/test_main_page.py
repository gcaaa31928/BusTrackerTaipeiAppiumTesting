__author__ = 'gca'
from tests.test_basic import BasicTestAppium

class MainPageTestAppium(BasicTestAppium):

    def setUp(self):
        super().setUp()

    def test_main_page_button_is_instance(self):
        self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('new UiSelector().text("Bicycle")'))
        self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('new UiSelector().text("MRT")'))
        self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('new UiSelector().text("Taxi")'))
        self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('new UiSelector().text("Railway")'))
        self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('new UiSelector().text("Tracker")'))
        self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('new UiSelector().text("Backup")'))
        self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('new UiSelector().text("Read me")'))
        self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('new UiSelector().text("Facebook")'))
        self.assertIsNotNone(self.driver.find_element_by_android_uiautomator('new UiSelector().text("Settings")'))

    # TODO(Red): routes, nearby, directions, favorites tests here

    def tearDown(self):
        super().tearDown()

