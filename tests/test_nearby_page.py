from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'gca'
from tests.test_basic import BasicTestAppium


class NearbyPageTestAppium(BasicTestAppium):
    def setUp(self):
        super().setUp()
        button = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Nearby")')
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
        first_stop = wait.until(
            lambda driver: self.driver.find_elements_by_id("nexti.android.bustaipei:id/text_stopname")
        )


    def test_all_info_is_corrective(self):
        self.input_place()
        wait = WebDriverWait(self.driver, 15)
        stop = wait.until(
            lambda driver: self.driver.find_element_by_id('nexti.android.bustaipei:id/text_stopname')
        )
        # Red: first stop is Huaisheng Elementary
        self.assertEqual(stop.text, 'Huaisheng Elementary School')

        # Red: first stop has correct routes
        stop_route = self.driver.find_element_by_id('nexti.android.bustaipei:id/text_routename').text
        self.assertEqual(stop_route, '669, 919')

        # Red: all stop is over 2 stops
        stop_count = len(self.driver.find_elements_by_id('nexti.android.bustaipei:id/drag_handle'))
        self.assertGreaterEqual(stop_count, 2)

    # TODO(Red): its image is kind of broken, i don't know how to test it.

    def tearDown(self):
        super().tearDown()
