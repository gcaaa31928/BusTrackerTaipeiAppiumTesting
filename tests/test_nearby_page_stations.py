from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.test_nearby_page import NearbyPageTestAppium
import re
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

    # TC100-05
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

    # TC100-06
    def test_sort_routes(self):
        wait = WebDriverWait(self.driver, 15)
        self.click_first_nearby_stop('Taipei Station')
        wait.until(
            lambda driver: self.driver.find_element_by_id('nexti.android.bustaipei:id/menu_passby_sort')
        ).click()
        sleep(0.5)
        estimates = self.driver.find_elements_by_id('nexti.android.bustaipei:id/text_estimate')
        current_estimate = 0
        is_depart = False
        for estimate in estimates:
            if is_depart:
                self.assertEqual(estimate.text, 'Depart')
            if estimate.text == 'Depart':
                is_depart = True
                continue
            elif estimate.text == 'Approach':
                continue
            match = re.search('(\d{0,2}) min', estimate.text)
            next_estimate = int(match.group(1))
            self.assertLessEqual(current_estimate, next_estimate)
            current_estimate = next_estimate

    # TC100-07
    def test_speaker_clock(self):
        wait = WebDriverWait(self.driver, 15)
        bus_text = self.click_bus_in_routes_page('Taipei Station', 0)
        speaker_clock = wait.until(
            lambda driver: self.driver.find_element_by_xpath("//android.widget.TextView[@text='Speacker clock']")
        )
        speaker_clock.click()
        title_text = wait.until(
            lambda driver: self.driver.find_element_by_id('nexti.android.bustaipei:id/text_routename')
        )
        self.assertEqual(bus_text, title_text.text)

    # TC100-08
    def test_route(self):
        pass

    def tearDown(self):
        super().tearDown()
