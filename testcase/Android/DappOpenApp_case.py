from appium import webdriver
import unittest
from PO.Android.DappOpenAppPage import DappOpenAppPage
from PO.Android.loginPage import LoginPage
from PO.basePage import Base
import time

class DappOpenAppTestCase(unittest.TestCase):
    """
    Dapp-开放平台app 测试用例
    """
    @classmethod
    def setUpClass(cls):
        # Base.android_driver_caps["noReset"] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        time.sleep(3)  # 等待初始化完成
        cls.login_page.check_in()
        cls.login_page.login_by_Email('xgq2@xinjineng.net', 'Abc123456') #调用登陆
        cls.open_app_page = DappOpenAppPage(cls.driver)

    def test_001_add_open_platform_App(self,type=u'APP'):
        '''
        用例一: 添加开放平台app
        :param type: 添加的类型
        '''
        try:
            self.open_app_page.dapp_page() #点击dapp菜单
            time.sleep(1)
            self.open_app_page.add_app_buisess(type) #添加app
            self.assertTrue(self.open_app_page.is_toast_exist('success'))
        except (BaseException,AssertionError):
            self.open_app_page.save_img("/open_add_app_fail")
            raise BaseException

    def test_002_App_Home(self):
        '''
        用例二: app的首页
        '''
        try:
            self.open_app_page.dapp_page() #点击dapp菜单
            time.sleep(1)
            self.assertTrue(self.open_app_page.click_app_home()) #app首页
        except (BaseException, AssertionError):
            self.open_app_page.save_img("/open_app_home_fail")
            raise BaseException

    def test_003_App_About_us(self):
        '''
        用例三: app的关于
        '''
        try:
            self.open_app_page.dapp_page() #点击dapp菜单
            time.sleep(1)
            self.assertTrue(self.open_app_page.click_About_us()) #app关于
        except (BaseException, AssertionError):
            self.open_app_page.save_img("/open_app_About_fail")
            raise BaseException

    def test_004_App_Home_Close(self):
        '''
        用例四: app首页关闭功能
        '''
        try:
            self.open_app_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.assertTrue(self.open_app_page.app_home_colse())
        except (BaseException, AssertionError):
            self.open_app_page.save_img("/open_close_app_fail")
            raise BaseException

    def test_005_Remove_App(self):
        '''
        用例五: 删除app
        '''
        try:
            self.open_app_page.dapp_page() #点击dapp菜单
            time.sleep(1)
            self.open_app_page.remove_app() #删除app
            self.assertTrue(self.open_app_page.is_toast_exist('success'))
        except (BaseException, AssertionError):
            self.open_app_page.save_img("/open_remove_app_fail")
            raise BaseException



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)