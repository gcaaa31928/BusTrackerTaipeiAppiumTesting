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
        self.click_first_stop()
        # Red: destination button is clickable
        click_destination_button = wait.until(
            EC.element_to_be_clickable((By.ID,'nexti.android.bustaipei:id/menu_passby_destination'))
        )
        self.assertIsNotNone(click_destination_button)
        passby_add_all = wait.until(
            EC.element_to_be_clickable((By.ID,'nexti.android.bustaipei:id/menu_passby_addall'))
        )
        self.assertIsNotNone(passby_add_all)
        passby_sort = wait.until(
            EC.element_to_be_clickable((By.ID,'nexti.android.bustaipei:id/menu_passby_sort'))
        )
        self.assertIsNotNone(passby_sort)

        stop_count = len(self.driver.find_elements_by_id('nexti.android.bustaipei:id/counter_view'))
        self.assertEqual(3, stop_count)

    def tearDown(self):
        super().tearDown()
