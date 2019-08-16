from appium import webdriver
import unittest
from PO.iOS.loginPage import LoginPage
from PO.basePage import Base
import time


@unittest.skip('ios端测试用例')
class LoginTestCase(unittest.TestCase):
    """
    登录的测试用例
    """

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.ios_driver_caps)  # 串联
        self.login_page = LoginPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(2)  # 等待初始化完成

    def test_login_by_email(self):
        """
        iOS端邮箱登录
        :return:
        """
        self.login_page.check_in()
        self.login_page.login_by_Email('476367003@xinjineng.net', 'Aa123456')
        time.sleep(10)

    def test_login_by_mobile(self):
        self.login_page.check_in()
        self.login_page.login_by_Mobile('4121580666', 'Aa123456')
        time.sleep(10)

    def tearDown(self):
        self.login_page.log_out()
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
