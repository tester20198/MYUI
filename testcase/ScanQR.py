from appium import webdriver
import unittest
from PO.loginPage import LoginPage
from PO.homePage import HomePage
from PO.basePage import Base
import time


@unittest.skip('test')
class ScanQRcode(unittest.TestCase):
    """
    扫码专项测试用例
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.driver_caps)  # 串联
        cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        cls.home_page = HomePage(cls.driver)

    def test_scan(self):
        time.sleep(3)
        self.login_page.login_by_Mobile('4126777777', 'Aa123456')
        self.login_page.login_in()
        time.sleep(3)
        s = 0
        for i in range(10):
            self.home_page.scanQR()
            s += 1
            print(f'第{s}次成功扫码...')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
