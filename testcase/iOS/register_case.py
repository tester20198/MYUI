from appium import webdriver
from PO.Android.registerPage import registerPage
from PO.basePage import Base
import unittest
import time


class RigisterTestCase(unittest.TestCase):
    """
    注册的测试用例
    """

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.ios_driver_caps)  # 串联
        self.register_page = registerPage(self.driver)  # 初始化登录页元素以及方法

    def test_register_by_mobile(self):
        self.register_page.click_register()
        self.register_page.register_by_mobile('China', '13765657769')
        self.register_page.verify()
        self.register_page.send_pwd()
        self.register_page.send_pay_pwd()
        self.register_page.save_img('tester.png')
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
