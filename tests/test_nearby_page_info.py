from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'gca'
from tests.test_basic import BasicTestAppium
from tests.test_nearby_page import NearbyPageTestAppium

class NearbyPageInfoTestAppium(NearbyPageTestAppium):
    def setUp(self):
        super().setUp()


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

        # Red: all stops can scrollable
        stops = self.driver.find_elements_by_id('nexti.android.bustaipei:id/drag_handle')
        self.driver.scroll(stops[-1], stops[0])


    def tearDown(self):
        super().tearDown()
