from appium import webdriver
import unittest
from PO.Android.registerPage import registerPage
from PO.basePage import Base
from Public.getLog import InsertLog,Screenshot
import time

class RigisterTestCase(unittest.TestCase):
    """
    注册的测试用例
    """

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        self.register_page = registerPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(3)  # 等待初始化完成
        self.imgs = []  # 截图列表

    # def add_img(self):
    #     # 截图方法
    #     self.imgs.append(self.driver.get_screenshot_as_base64())
    #     return True

    def test_mobile_register(self):
        '''手机注册'''
        self.register_page.click_register()
        self.register_page.register_by_mobile("Venezuela","4125211666",'Abc123456','123456','2222')
        # self.register_page.save_img('registermobile.png')
        self.register_page.click_confirm_button()

    def test_email_register(self):
        '''邮箱注册'''
        self.register_page.click_register()
        self.register_page.register_by_eamil('Venezuela','121323232@qq.com','Abc123456','123456','2222')
        # self.register_page.save_img('registeremail.png')
        self.register_page.click_confirm_button()

    def test_register_Agreement(self):
        '''
        用例三: 点击注册界面的协议，判断注册页面跳转到登录页面时，获取忘记密码的文本
        '''
        try:
            self.register_page.click_register()
            msg = self.register_page.clcik_register_Agreement()
            self.assertEqual(msg, u'Forgot password1')
            print('从注册页面跳转到登录页面,获取的页面文本信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.driver)
            InsertLog().debug(msg)
            raise BaseException


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
