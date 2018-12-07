from appium import webdriver
import unittest
from PO.loginPage import LoginPage
from PO.basePage import Base
import time


class LoginTestCase(unittest.TestCase):
    """
    登录的测试用例
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.driver_caps)  # 串联
        cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法

    def test_login_by_email(self):
        time.sleep(3)
        self.login_page.login_by_Email('476367001@qq.com', 'Aa123456')  # 邮箱登录
        self.login_page.login_in()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()