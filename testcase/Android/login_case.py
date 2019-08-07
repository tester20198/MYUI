from appium import webdriver
import unittest
from PO.Android.loginPage import LoginPage
from PO.basePage import Base
from Public.other import create_address
import time

create_login_password = create_address(8) #随机生成8位的登陆密码

class LoginTestCase(unittest.TestCase):
    """
    登录的测试用例
    """

    def setUp(self):
        Base.android_driver_caps["noReset"] = False
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        self.login_page = LoginPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(3)  # 等待初始化完成

    def test_001_help_and_feedback(self):
        '''
        用例一: 登陆界面工单系统
        '''
        try:
            self.login_page.check_in()
            time.sleep(2)
            msg,msg1,msg2 = self.login_page.help_and_feedback()
            # msg 为FAQ菜单的标题，msg1为Support and Feedback菜单的标题，msg2为Disclaimer菜单的标题
            self.assertListEqual([msg,msg1,msg2],['FAQ','Support and Feedback','Disclaimer'])
            print('工单系统点击各个菜单后,获取的页面标题: %s'% msg,msg1,msg2)
        except (BaseException, AssertionError):
            self.login_page.save_img("/help_and_feedback_fail")
            raise BaseException

    def test_002_login_by_email(self):
        '''
        用例二: 邮箱登陆
        '''
        try:
            self.login_page.check_in()
            time.sleep(2)
            self.login_page.login_by_Email('476367003@xinjineng.net', 'Aa123456')
            msg = self.login_page.Dapp_balance_text()  # 断言登陆成功后，获取Dapp页面Balance的文本信息
            self.assertEqual(msg, u'Balance')
            print('登陆成功后,获取Dapp页面文本信息：%s' % msg)
        except (BaseException, AssertionError):
            self.login_page.save_img("/login_by_email_fail")
            raise BaseException

    def test_003_login_by_mobile(self):
        '''
        用例三: 手机号码登陆
        '''
        try:
            self.login_page.check_in()
            time.sleep(2)
            self.login_page.login_by_Mobile('4121580666', 'Aa123456', na='Venezuela')
            msg = self.login_page.Dapp_balance_text()  #断言登陆成功后，获取Dapp页面Balance的文本信息
            self.assertEqual(msg,u'Balance')
            print('登陆成功后,获取Dapp页面文本信息：%s' % msg)
        except (BaseException, AssertionError):
            self.login_page.save_img("/login_by_mobile_fail")
            raise BaseException

    def test_004_Email_Forgot_password(self):
        '''
        用例四: 单邮箱忘记密码
        '''
        try:
            self.login_page.check_in()
            time.sleep(2)
            msg = self.login_page.Email_Forgot_password('76163348@qq.com','2222',create_login_password)
            self.assertEqual(msg,u'Log In')
            print('登陆密码重置成功,获取登陆页面login按钮文本信息：%s' % msg)  # 重置成功后，获取登陆界面的Log in按钮文本信息
        except (BaseException, AssertionError):
            self.login_page.save_img("/Email_Forgot_password_fail")
            raise BaseException

    def test_005_Mobile_Forgot_password(self):
        '''
        用例五: 单手机忘记密码
        '''
        try:
            self.login_page.check_in()
            time.sleep(2)
            msg = self.login_page.Mobile_Forgot_password('4121234567', '2222', create_login_password,na='Venezuela')
            self.assertEqual(msg, u'Log In')
            print('登陆密码重置成功,获取登陆页面login按钮文本信息：%s' % msg)  # 重置成功后，获取登陆界面的Log in按钮文本信息
        except (BaseException, AssertionError):
            self.login_page.save_img("/Mobile_Forgot_password_fail")
            raise BaseException

    def test_006_login_Sign_Up(self):
        '''
        用例六: 登陆界面点击Sign Up跳转注册界面
        '''
        try:
            self.login_page.check_in()
            time.sleep(2)
            msg = self.login_page.click_loginpage_SignUp()
            self.assertTrue(msg)
            print('从登陆页面跳转到注册页面,获取的页面文本信息：%s' % msg)  # 获取支付密码的文本信息
        except (BaseException, AssertionError):
            self.login_page.save_img("/login_Sign_Up_fail")
            raise BaseException

    def tearDown(self):
        # self.driver.back()
        # self.login_page.log_out()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)
