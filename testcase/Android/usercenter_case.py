from appium import webdriver
import unittest
from PO.Android.loginPage import LoginPage
from PO.Android.usercenterPage import UsercenterPage
from PO.basePage import Base
from appium.webdriver.mobilecommand import MobileCommand
from Public.getLog import write_log, stop_log
import time


class UsercenterTestCase(unittest.TestCase):
    """
    个人中心的测试用例
    """

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        self.login_page = LoginPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(3)
        self.user_page = UsercenterPage(self.driver)  # 初始化个人中心页元素以及方法
        time.sleep(3)  # 等待初始化完成


    def test_into_Vouchers(self):
        """ 个人中心 - 优惠券
        路径：优惠券 -- 查看无可用优惠券 -- 查看优惠券说明

        """
        time.sleep(3)
        self.login_page.enter_usercenter()
        time.sleep(3)
        self.user_page.my_vouchers()




    def test_setting_kyc(self):
        """设置KYC
        路径 ： 配置KYC 第一页数据
        """
        time.sleep(3)
        self.login_page.enter_usercenter()
        time.sleep(2)
        self.user_page.setting_kyc('first','second','third','6742384')



    def test_into_change_phone(self):
        """设置 -- 修改手机号
        路径 ：获取验证码 -- 输入新号 -- 提交
        """
        time.sleep(3)
        self.login_page.enter_usercenter()
        time.sleep(3)
        self.user_page.change_phone(2222,4120909090)
        time.sleep(3)







    # def test_into_collection(self):
    #     self.login_page.check_in()
    #     self.login_page.login_by_Email('uat-2.0626@jianglun.xinjineng.net', 'Test1234')
    #     time.sleep(10)
    #     self.driver.back()
    #     time.sleep(3)
    #     self.user_page.into_Collection()  # 进入收款页面
    #
    # def test_into_assets(self):
    #     self.login_page.check_in()
    #     self.login_page.login_by_Email('uat-2.0626@jianglun.xinjineng.net', 'Test1234')
    #     time.sleep(10)
    #     self.driver.back()
    #     self.login_page.enter_usercenter()
    #     time.sleep(3)
    #     self.user_page.into_Assets()  # 进入资产页面
    #
    # def test_into_bill(self):
    #     self.login_page.check_in()
    #     self.login_page.login_by_Email('uat-2.0626@jianglun.xinjineng.net', 'Test1234')
    #     time.sleep(10)
    #     self.driver.back()
    #     self.login_page.enter_usercenter()
    #     time.sleep(3)
    #     self.user_page.into_Bill()  # 进入账单页面
    # #
    # def test_into_coupon(self):
    #     self.login_page.check_in()
    #     self.login_page.login_by_Email('uat-2.0626@jianglun.xinjineng.net', 'Test1234')
    #     time.sleep(10)
    #     self.driver.back()
    #     self.login_page.enter_usercenter()
    #     time.sleep(3)
    #     self.user_page.into_coupon()  # 进入优惠券页面
    #
    # def test_into_kyc(self):
    #     self.login_page.check_in()
    #     self.login_page.login_by_Email('uat-2.0626@jianglun.xinjineng.net', 'Test1234')
    #     time.sleep(10)
    #     self.driver.back()
    #     self.login_page.enter_usercenter()
    #     time.sleep(3)
    #     self.user_page.into_KYC()  # 进入KYC页面
    #
    # def test_into_setting(self):
    #     self.login_page.check_in()
    #     self.login_page.login_by_Email('uat-2.0626@jianglun.xinjineng.net', 'Test1234')
    #     time.sleep(10)
    #     self.driver.back()
    #     self.login_page.enter_usercenter()
    #     time.sleep(3)
    #     self.user_page.into_setting()  # 进入设置页面
    #
    # def test_into_merchant(self):
    #     self.login_page.check_in()
    #     self.login_page.login_by_Email('uat-2.0626@jianglun.xinjineng.net', 'Test1234')
    #     time.sleep(10)
    #     self.driver.back()
    #     self.login_page.enter_usercenter()
    #     time.sleep(3)
    #     self.user_page.into_merchant()  # 进入商户中心页面
    #
    # def test_into_feedback(self):
    #     self.login_page.check_in()
    #     self.login_page.login_by_Email('uat-2.0626@jianglun.xinjineng.net', 'Test1234')
    #     time.sleep(10)
    #     self.driver.back()
    #     self.login_page.enter_usercenter()
    #     time.sleep(3)
    #     self.user_page.into_help()  # 进入feedback页面

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
