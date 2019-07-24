from appium import webdriver
import unittest
from PO.Android.loginPage import LoginPage
from PO.Android.dappFxPage import DappPage
from PO.basePage import Base
from PO.basePage import Base
from selenium.webdriver.common.by import By
import time
from Public.getLog import write_log, stop_log
import time
import PO.Android.dappFxPage



class DAppFxTestCase(unittest.TestCase):
    """
    DAPP的测试用例
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        time.sleep(5)  # 等待初始化完成
        cls.dapp_Page=DappPage(cls.driver) #初始化dapp页的元素以及方法
        time.sleep(5)

        # cls.login_page.check_in()
        # time.sleep(3)
        # cls.login_page.login_by_Email('dengjh_123456@163.com', 'Test123456')
        # time.sleep(5)


    #
    # """
    # 登录邮箱账号为：dengjh_123456@163.com
    # """
    # # @unittest.skip
    # def test_login_by_email(self):
    #     self.login_page.check_in()
    #     time.sleep(3)
    #     self.login_page.login_by_Email('dengjh_123456@163.com', 'Test123456')
    #     time.sleep(10)
    #     self.login_page.click2('Skip')  # 登录成功后，点击红包引导界面的"跳过"按钮


    """
    点击添加卡片按钮
    """
    # def test_add_FXCard(self):
        # # if self.login_page.findElement("Skip"):
        # #     self.login_page.click2('Skip')  # 登录成功后，点击红包引导界面的"跳过"按钮
        # #     time.sleep(2)
        #
        #
        # # self.dapp_Page.enter_dapp()#点击Dapp按钮
        # time.sleep(2)
        # self.dapp_Page.add_fxcard()
        # time.sleep(3)

    def test_click_fx_setting(self):
        """
        进入fx_setting
        """
        #self.login_page.click2("FX")
        self.dapp_Page.click2(self.dapp_Page.Dapp_enter_fx_card)
        time.sleep(2)
        self.dapp_Page.enter_fx_setting()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    def test_conversion(self):
        """
        进入conversion界面
        """
        #self.login_page.click2("Conversion")
        self.dapp_Page.click2(self.dapp_Page.fx_conversion_btn)
        time.sleep(4)
        self.driver.find_element_by_id(self.dapp_Page.conver_option_btn)
        time.sleep(2)



if __name__ == '__main__':
        unittest.main(verbosity=0)