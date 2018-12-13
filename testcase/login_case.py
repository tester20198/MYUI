from appium import webdriver
import unittest
from PO.loginPage import LoginPage
from PO.basePage import Base
from Public.getLog import write_log,stop_log
import time



class LoginTestCase(unittest.TestCase):
    """
    登录的测试用例
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.driver_caps)  # 串联
        cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        cls.imgs = []
        write_log()

    @unittest.skip('调试')
    def test_login_by_email(self):
        time.sleep(3)
        self.login_page.login_by_Email('476367001@qq.com', 'Aa123456')  # 邮箱登录
        self.login_page.login_in()
        time.sleep(3)

    def add_img(self):
        # 在是python3.x中，如果在这里初始化driver，因为3.x版本unittest运行机制不同，会导致用力失败时截图失败
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def test_login_by_mobile(self):
        time.sleep(3)
        self.login_page.login_by_Mobile('4126777777', 'Aa123456')
        self.login_page.login_in()
        # time.sleep(5)
        # self.add_img()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        stop_log()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()