__author__ = 'gca'
from tests.test_basic import BasicTestAppium

class PackageTestAppium(BasicTestAppium):

    def setUp(self):
        super().setUp()

    def test_installed(self):
        self.assertFalse(self.driver.is_app_installed('is.not.existed.app'))
        self.assertTrue(self.driver.is_app_installed('nexti.android.bustaipei'))

    def test_removed(self):
        self.assertTrue(self.driver.is_app_installed('nexti.android.bustaipei'))
        self.driver.remove_app('nexti.android.bustaipei')
        self.assertFalse(self.driver.is_app_installed('nexti.android.bustaipei'))


    # def test_ClickRefreshLink(self):
    #     el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("路線規劃")')
    #     el.click()
        # refreshButton  = self.driver.find_element_by_id("com.witmergers.getstatus:id/fab")
        # self.assertTrue(refreshButton.is_displayed())
        # refreshButton.click()
        # ## Right now we are just verify the displayed message on the Phone
        # ## You can right code to handle that toast message and Verify that message

    def tearDown(self):
        super().tearDown()

# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(PackageTestAppium)
#     unittest.TextTestRunner(verbosity=2).run(suite)
