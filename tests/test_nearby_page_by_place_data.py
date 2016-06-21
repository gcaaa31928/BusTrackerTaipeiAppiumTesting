from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
import csv
import random

__author__ = 'gca'
from tests.test_basic import BasicTestAppium
from tests.test_nearby_page import NearbyPageTestAppium


class NearbyPageByPlaceDataTestAppium(NearbyPageTestAppium):
    def setUp(self):
        super().setUp()

    # TC100-11 Place Data
    def test_place_data(self):
        self.go_to_searching_location_page()
        place_list = []
        with open("../data/place_name.csv", encoding='utf8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                place_list.append(row[0])
        for i in range(0, 30):
            expected_place_name = random.choice(place_list)
            actual_place_name = self.get_first_search_place_name(expected_place_name)
            print(expected_place_name, actual_place_name)
            self.assertTrue(expected_place_name in actual_place_name,
                            "預期的名字為 " + expected_place_name + "，但實際的名字為 " + actual_place_name)

    def tearDown(self):
        super().tearDown()
