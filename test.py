from Tools.scripts.win_add2path import PATH

__author__ = 'gca'
import os
import unittest
from appium import webdriver
''' ScrollTest.com by Promode '''
''' This Test Case Just Click on the Refresh Button My Application '''
''' Just Click and Verify it in you Phone '''
''' Copyright 2015 '''

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class ContactAppTestAppium(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android'
        desired_caps['app'] = PATH('bus.apk')
        desired_caps['appPackage'] = 'nexti.android.bustaipei'
        desired_caps['appActivity'] = 'nexti.android.bustaipei.activities.SplashActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_ClickRefreshLink(self):
        pass
        # refreshButton  = self.driver.find_element_by_id("com.witmergers.getstatus:id/fab")
        # self.assertTrue(refreshButton.is_displayed())
        # refreshButton.click()
        # ## Right now we are just verify the displayed message on the Phone
        # ## You can right code to handle that toast message and Verify that message

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)