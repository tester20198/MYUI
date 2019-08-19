from appium import webdriver
import unittest
from PO.Android.RegisterPage import registerPage
from PO.basePage import Base
from Public.other import create_email,create_mobile
from BeautifulReport import BeautifulReport
import time


class RigisterTestCase(unittest.TestCase):
    """
    注册的测试用例
    """

    def setUp(self):
        Base.android_driver_caps["noReset"] = False
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        self.register_page = registerPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(5)  # 等待初始化完成

    @BeautifulReport.add_img('001_mobile_register_fail')
    def test_001_mobile_register(self,nation='Venezuela',loginpwd='Abc123456',paypwd='123456',code='2222'):
        '''
        用例一： 手机注册
        :param nation: 传参国家名称，默认委内瑞拉
        :param create_mobile: 传参手机号码，create_mobile 随机生成委内瑞拉手机号码
        :param loginpwd: 登陆密码
        :param paypwd:   交易密码
        :param code:  手机验证码
        :return:
        '''
        try:
            mobile = create_mobile()  # 随机生成委内瑞拉手机号码
            self.register_page.click_register()  # Venezuela
            self.register_page.register_by_mobile(nation,mobile,loginpwd,paypwd,code)
            msg = self.register_page.click_confirm_button()
            self.assertTrue(msg)
            print('注册成功后跳转到设置用户头像界面,获取的头像字段文本信息：%s' % msg)
        except (Exception, AssertionError):
            self.register_page.save_img("001_mobile_register_fail")
            raise Exception

    @BeautifulReport.add_img('002_email_register_fail')
    def test_002_email_register(self,loginpwd='Abc123456',paypwd='123456',code='2222'):
        """
        用例二： 邮箱注册
        :param create_email: 传参邮箱地址，create_email随机生成地址
        :param loginpwd: 登陆密码
        :param paypwd:   交易密码
        :param code:  邮箱验证码
        :return:
        """
        try:
            email = create_email()  # 随机生成邮箱地址
            self.register_page.click_register()
            self.register_page.register_by_eamil(email,loginpwd,paypwd,code)
            msg = self.register_page.click_confirm_button()
            self.assertTrue(msg)
            print('注册成功后跳转到设置用户头像界面,获取的头像字段文本信息：%s' % msg)
        except (Exception,AssertionError):
            self.register_page.save_img("002_email_register_fail")
            raise Exception

    @BeautifulReport.add_img('003_register_fail')
    def test_003_register_Agreement(self):
        """
        用例三: 点击注册界面的协议和判断注册页面跳转到登录页面时，获取忘记密码的文本
        """
        try:
            self.register_page.click_register()
            msg = self.register_page.clcik_register_Agreement()
            self.assertEqual(msg, u'Forgot password')
            print('从注册页面跳转到登录页面,获取的页面文本信息：%s' % msg)
        except (Exception,AssertionError):
            self.register_page.save_img("003_register_fail")
            raise Exception

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)