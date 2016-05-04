__author__ = 'gca'
import os
import unittest
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class BasicTestAppium(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android'
        desired_caps['app'] = PATH('../bus.apk')
        desired_caps['appPackage'] = 'nexti.android.bustaipei'
        desired_caps['appActivity'] = 'nexti.android.bustaipei.activities.SplashActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
