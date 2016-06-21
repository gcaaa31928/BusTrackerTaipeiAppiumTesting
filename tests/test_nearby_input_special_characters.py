import random
import string
import unicodedata
from selenium.webdriver.support.wait import WebDriverWait

from tests.test_nearby_page import NearbyPageTestAppium

__author__ = 'gca'
from tests.test_basic import BasicTestAppium


class NearbyPageTestAppium(NearbyPageTestAppium):
    def setUp(self):
        super().setUp()

    def test_input_special_character(self):
        self.input_random_special_characters(length=15)

    def test_input_length(self):
        self.input_random_special_characters(length=255)

    def input_random_special_characters(self, length):
        try:
            wait = WebDriverWait(self.driver, 5)
            random_special_character = ''

            random_section = [(0,31),(55424, 56255), (14727297,14727354), (4036988032,4036990911), (4036991104,4036991375)]  # control, arabic, thai, special, emoji

            for pos in range(1, length, 1):

                choice_range_min = random_section[1][0]
                choice_range_max = random_section[1][1]
                random_special_character += chr(random.choice(range(choice_range_min,choice_range_max,1)))

            self.go_to_searching_location_page()
            first_result = self.get_first_search_place_name(random_special_character)
        except:
            self.assertTrue(False, '出現無法預期的錯誤')

    def tearDown(self):
        super().tearDown()
