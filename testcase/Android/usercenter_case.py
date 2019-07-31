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

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        time.sleep(5)  # 等待初始化完成
        cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        cls.login_page.check_in()
        time.sleep(1)
        cls.login_page.login_by_Email(' 476367003@xinjineng.net', 'Aa123456')
        time.sleep(5)
        cls.user_page = UsercenterPage(cls.driver)  # 初始化个人中心页元素以及方法
        cls.user_page.go_to_usercenter()
        time.sleep(1)


    def test_into_Vouchers(self):
        """ 我的优惠券"""
        time.sleep(3)
        self.user_page.my_vouchers()


    def test_setting_kyc(self):
        """设置KYC-第一页"""
        time.sleep(2)
        self.user_page.setting_kyc('first','second','third','6742384')

    def test_into_change_phone(self):
        """设置 -- 修改手机号"""
        time.sleep(3)
        self.user_page.change_phone(2222,4120909090)
        time.sleep(3)


    def test_change_email(self):
        """ 修改邮箱地址"""
        self.user_page.enter_usercenter()
        time.sleep(3)
        self.user_page.change_email(2222,'120@qq.com')


    def test_general(self):
        """通用 - 语言及货币选择 """
        self.user_page.enter_usercenter()
        time.sleep(2)
        self.user_page.general()
    #

    # def test_change_loginPWD(self):
    #     """"修改登录密码"""
    #     self.user_page.enter_usercenter()
    #     time.sleep(2)
    #     self.user_page.change_login_paw('Test1234')
    #
    # def test_change_payPwd(self):
    #     """修改支付密码"""
    #     self.user_page.enter_usercenter()
    #     time.sleep(2)
    #     self.user_page.change_payPwd('123456')
    #
    #
    # def test_forget_pay_password(self):
    #     """忘记支付密码"""
    #     self.user_page.enter_usercenter()
    #     time.sleep(2)
    #     self.user_page.forget_pay_password(2222)


    # def test_pattern(self):
    #     """设置-手势密码"""
    #     self.user_page.enter_usercenter()
    #     time.sleep(3)
    #     self.user_page.pattern()
    #

    # def test_fingerprint(self):
    #     """设置-指纹识别"""
    #     self.user_page.enter_usercenter()
    #     time.sleep(3)
    #     self.user_page.fingerprint()


    # def test_google(self):
    #     """谷歌验证码"""
    #     self.user_page.enter_usercenter()
    #     time.sleep(3)
    #     self.user_page.google(2222)





    def test_001_check_code(self):
        self.user_page.into_Collection()  # 进入收款页面
        time.sleep(1)
        self.assertTrue(self.user_page.check_QR_code(), '判断是否加载收款二维码成功')

    def test_002_save_code(self):
        # self.user_page.into_Collection()  # 进入收款页面
        time.sleep(1)
        self.user_page.save_QRcode()
        self.assertTrue(self.user_page.is_toast_exist('Image'), '判断是否保存收款二维码成功')

    def test_003_collection_history(self):
        # self.user_page.into_Collection()  # 进入收款页面
        time.sleep(1)
        self.user_page.check_collection_history()
        time.sleep(1)
        self.assertTrue(self.user_page.findElement('Status'), '判断是否加载收款详情成功')
        self.assertFalse(self.user_page.is_toast_exist('Sever'), '判断是否出现500')






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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
