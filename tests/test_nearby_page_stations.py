from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.test_nearby_page import NearbyPageTestAppium

__author__ = 'gca'
from tests.test_basic import BasicTestAppium


class NearbyPageStationTestAppium(NearbyPageTestAppium):
    def setUp(self):
        super().setUp()

    # TC100-02
    def test_all_button_is_clickable(self):
        wait = WebDriverWait(self.driver, 15)
        self.click_first_nearby_stop('no. 8, section 3, civic blvd')
        # Red: destination button is clickable
        click_destination_button = wait.until(
            EC.element_to_be_clickable((By.ID, 'nexti.android.bustaipei:id/menu_passby_destination'))
        )
        self.assertIsNotNone(click_destination_button)
        passby_add_all = wait.until(
            EC.element_to_be_clickable((By.ID, 'nexti.android.bustaipei:id/menu_passby_addall'))
        )
        self.assertIsNotNone(passby_add_all)
        passby_sort = wait.until(
            EC.element_to_be_clickable((By.ID, 'nexti.android.bustaipei:id/menu_passby_sort'))
        )
        self.assertIsNotNone(passby_sort)

        stop_count = len(self.driver.find_elements_by_id('nexti.android.bustaipei:id/counter_view'))
        self.assertEqual(3, stop_count)

    # TC100-03
    def test_search_station(self):
        expected_routes = ['221', '232', '232', 'F215去', 'F215返', 'F216去', 'F216返', 'F223工業去', 'F223工業返', 'F223去']
        wait = WebDriverWait(self.driver, 15)
        self.click_first_nearby_stop('Taipei Station')
        stop_title = wait.until(
            lambda driver: self.driver.find_element_by_xpath("//android.widget.TextView[@text='Taipei Main Sta.']")
        )
        routes = self.driver.find_elements_by_id('nexti.android.bustaipei:id/text_routename')
        index = 0
        for route in routes:
            self.assertTrue(expected_routes[index] in route.text)
            index += 1

    # TC100-04
    def test_add_favorites_station(self):
        wait = WebDriverWait(self.driver, 15)
        self.click_bus_in_routes_page('Taipei Station', 0)
        add_favorites_button = wait.until(
            lambda driver: self.driver.find_element_by_xpath("//android.widget.TextView[@text='Add']")
        )
        add_favorites_button.click()
        submit = wait.until(
            lambda driver: self.driver.find_element_by_id('android:id/button1')
        )
        submit.click()
        sleep(1)
        self.driver.press_keycode(4)
        sleep(1)
        self.driver.press_keycode(4)
        self.click_favorites_page()
        first_favorites_stop = wait.until(
            lambda dirver: self.driver.find_element_by_id('nexti.android.bustaipei:id/text_stopname')
        )
        self.assertEqual(first_favorites_stop.text, 'Taipei Main Sta.')

    def test_route_info(self):
        wait = WebDriverWait(self.driver, 15)
        self.click_bus_in_routes_page('Taipei Station', 0)
        timetable_button = wait.until(
            lambda driver: self.driver.find_element_by_xpath("//android.widget.TextView[@text='Timetable']")
        )
        timetable_button.click()
        title = wait.until(
            lambda driver: self.driver.find_element_by_xpath("//android.widget.TextView[@index='1']")
        ).text
        self.assertEqual(title, 'Route info')


    def tearDown(self):
            super().tearDown()
