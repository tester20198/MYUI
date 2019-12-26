from appium import webdriver
from Page.iOS.loginPage import LoginPage
from Page.basePage import Base
import pytest
import time


@pytest.skip('ios端测试用例')
class TestLogin_ios:
    """
    登录的测试用例
    """

    def setup_method(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.ios_driver_caps)  # 串联
        self.login_page = LoginPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(2)  # 等待初始化完成

    def test_001_login_by_email(self):
        """
        iOS端邮箱登录
        :return:
        """
        self.login_page.check_in()
        self.login_page.login_by_Email('476367003@xinjineng.net', 'Aa123456')
        time.sleep(10)

    def test_002_login_by_mobile(self):
        self.login_page.check_in()
        self.login_page.login_by_Mobile('4121580666', 'Aa123456')
        time.sleep(10)

    def teardown_method(self):
        self.login_page.log_out()
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
