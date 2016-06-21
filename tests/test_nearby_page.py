import re
from time import sleep

from selenium.common.exceptions import TimeoutException
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

    def click_favorites_page(self):
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(
            lambda driver: self.driver.find_element_by_android_uiautomator('new UiSelector().text("Favorites")')
        )
        button.click()

    def go_to_searching_location_page(self):
        wait = WebDriverWait(self.driver, 15)
        input = wait.until(
            lambda driver: self.driver.find_element_by_id("nexti.android.bustaipei:id/text_place")
        )
        input.click()

    def get_first_search_place_name(self, place_name):
        wait = WebDriverWait(self.driver, 15)
        input_place = wait.until(
            lambda driver: self.driver.find_element_by_id("nexti.android.bustaipei:id/edit_place")
        )
        input_place.send_keys(place_name)
        self.driver.find_element_by_id('nexti.android.bustaipei:id/button_go').click()
        wait = WebDriverWait(self.driver, 15)
        first_nearby_stop = wait.until(
            lambda driver: self.driver.find_element_by_id('nexti.android.bustaipei:id/text_name')
        )
        return first_nearby_stop.text

    def click_first_search_place(self, place_name):
        wait = WebDriverWait(self.driver, 15)
        input = wait.until(
            lambda driver: self.driver.find_element_by_id("nexti.android.bustaipei:id/text_place")
        )
        input.click()
        input_place = wait.until(
            lambda driver: self.driver.find_element_by_id("nexti.android.bustaipei:id/edit_place")
        )
        input_place.send_keys(place_name)
        self.driver.find_element_by_id('nexti.android.bustaipei:id/button_go').click()
        wait = WebDriverWait(self.driver, 15)
        first_nearby_stop = wait.until(
            lambda driver: self.driver.find_element_by_id('nexti.android.bustaipei:id/text_name')
        ).click()

    def click_first_nearby_stop(self, place_name):
        self.click_first_search_place(place_name)
        wait = WebDriverWait(self.driver, 15)
        first_nearby_stop = wait.until(
            lambda driver: self.driver.find_element_by_xpath("//android.widget.TextView[@index='0' and @resource-id='nexti.android.bustaipei:id/text_stopname']")
        )
        first_nearby_stop.click()

    def click_bus_in_routes_page(self, place_name, bus_index):
        self.click_first_nearby_stop(place_name)
        wait = WebDriverWait(self.driver, 15)
        bus = wait.until(
            lambda driver: self.driver.find_elements_by_id('nexti.android.bustaipei:id/text_routename')
        )[bus_index]
        bus_text = bus.text
        bus.click()
        return bus_text

    def clear_all_notifications(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.open_notifications()
        try:
            dismiss_button = wait.until(
                lambda driver: self.driver.find_element_by_id('com.android.systemui:id/dismiss_text')
            )
            dismiss_button.click()
            cancel_alarm_button = wait.until(
                lambda driver: self.driver.find_element_by_xpath("//android.widget.Button[@text='Cancel alarm']")
            )
            cancel_alarm_button.click()
        except:
            pass
        finally:
            self.driver.press_keycode(4)

    def tearDown(self):
        super().tearDown()
