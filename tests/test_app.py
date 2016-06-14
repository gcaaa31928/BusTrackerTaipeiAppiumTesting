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



    def tearDown(self):
        super().tearDown()

# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(PackageTestAppium)
#     unittest.TextTestRunner(verbosity=2).run(suite)
