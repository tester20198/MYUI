from appium import webdriver
from Page.Android.DappOpenAppPage import DappOpenAppPage
from Page.basePage import Base
import pytest
import time


@pytest.mark.skip('未调试完成')
class TestOpenPlatformApp:
    """
    Dapp-开放平台app 测试用例
    """

    def setup_class(self):
        self.appname = u'P Demo'  # 必须传参app名称
        Base.android_driver_caps["noReset"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        time.sleep(3)  # 等待初始化完成
        self.open_app_page = DappOpenAppPage(self.driver)

    def test_001_add_open_platform_App(self):
        '''
        用例一: 添加开放平台app
        :param type: 添加的类型
        '''
        try:
            self.open_app_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.open_app_page.add_app_buisess(self.appname)  # 添加app
            self.assertTrue(self.open_app_page.is_toast_exist('success'))
        except (Exception, AssertionError):
            self.open_app_page.save_img("open_add_app_fail")
            raise Exception

    def test_002_App_Home(self):
        '''
        用例二: app的首页
        '''
        try:
            self.open_app_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.assertTrue(self.open_app_page.click_app_home())  # app首页
        except (Exception, AssertionError):
            self.open_app_page.save_img("open_app_home_fail")
            raise Exception

    def test_003_App_About_us(self):
        '''
        用例三: app的关于
        '''
        try:
            self.open_app_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.assertTrue(self.open_app_page.click_About_us())  # app关于
        except (Exception, AssertionError):
            self.open_app_page.save_img("open_app_About_fail")
            raise Exception

    def test_004_App_Home_Close(self):
        '''
        用例四: app首页关闭功能
        '''
        try:
            self.open_app_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.assertTrue(self.open_app_page.app_home_colse())
        except (Exception, AssertionError):
            self.open_app_page.save_img("open_close_app_fail")
            raise Exception

    def test_005_Remove_App(self):
        '''
        用例五: 删除app
        '''
        try:
            self.open_app_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.open_app_page.remove_app()  # 删除app
            self.assertTrue(self.open_app_page.is_toast_exist('success'))
        except (Exception, AssertionError):
            self.open_app_page.save_img("open_remove_app_fail")
            raise Exception

    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
