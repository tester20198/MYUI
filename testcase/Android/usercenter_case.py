from appium import webdriver
import unittest
from PO.Android.loginPage import LoginPage
from PO.Android.usercenterPage import UsercenterPage
from PO.basePage import Base
from appium.webdriver.mobilecommand import MobileCommand
from Public.getLog import write_log, stop_log
import time


class LoginTestCase(unittest.TestCase):
    """
    登录的测试用例
    """

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        self.login_page = LoginPage(self.driver)  # 初始化登录页元素以及方法
        self.user_page = UsercenterPage(self.driver)  # 初始化个人中心页元素以及方法
        time.sleep(3)  # 等待初始化完成
        self.imgs = []  # 截图列表

    def add_img(self):
        # 截图方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True


    def test_into_collection(self):
        self.login_page.check_in()
        self.login_page.login_by_Email('476367003@xinjineng.net', 'Aa123456')
        time.sleep(10)
        #self.driver.implicitly_wait(10)
        #self.driver.save_screenshot('/Users/pundix047/PycharmProjects/MYUI/img/home.png')
        self.driver.back()
        self.login_page.into_extra()
        print(self.driver.contexts)
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.pundix.xwallet"})
        print(self.driver.current_context)
        time.sleep(4)
        print(self.driver.page_source)
        time.sleep(3)
        #self.user_page.into_Collection()  # 进入收款页面

    def test_into_assets(self):
        self.login_page.check_in()
        self.login_page.login_by_Email('476367003@xinjineng.net', 'Aa123456')
        time.sleep(10)
        self.driver.back()
        self.login_page.enter_usercenter()
        time.sleep(3)
        self.user_page.into_Assets()  # 进入资产页面

    def test_into_bill(self):
        self.login_page.check_in()
        self.login_page.login_by_Email('476367003@xinjineng.net', 'Aa123456')
        time.sleep(10)
        self.driver.back()
        self.login_page.enter_usercenter()
        time.sleep(3)
        self.user_page.into_Bill()  # 进入账单页面

    def test_into_coupon(self):
        self.login_page.check_in()
        self.login_page.login_by_Email('476367003@xinjineng.net', 'Aa123456')
        time.sleep(10)
        self.driver.back()
        self.login_page.enter_usercenter()
        time.sleep(3)
        self.user_page.into_coupon()  # 进入优惠券页面

    def test_into_kyc(self):
        self.login_page.check_in()
        self.login_page.login_by_Email('476367003@xinjineng.net', 'Aa123456')
        time.sleep(10)
        self.driver.back()
        self.login_page.enter_usercenter()
        time.sleep(3)
        self.user_page.into_KYC()  # 进入KYC页面

    def test_into_setting(self):
        self.login_page.check_in()
        self.login_page.login_by_Email('476367003@xinjineng.net', 'Aa123456')
        time.sleep(10)
        self.driver.back()
        self.login_page.enter_usercenter()
        time.sleep(3)
        self.user_page.into_setting()  # 进入设置页面

    def test_into_merchant(self):
        self.login_page.check_in()
        self.login_page.login_by_Email('476367003@xinjineng.net', 'Aa123456')
        time.sleep(10)
        self.driver.back()
        self.login_page.enter_usercenter()
        time.sleep(3)
        self.user_page.into_merchant()  # 进入商户中心页面

    def test_into_feedback(self):
        self.login_page.check_in()
        self.login_page.login_by_Email('476367003@xinjineng.net', 'Aa123456')
        time.sleep(10)
        self.driver.back()
        self.login_page.enter_usercenter()
        time.sleep(3)
        self.user_page.into_help()  # 进入feedback页面

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
