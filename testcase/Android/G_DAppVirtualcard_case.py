from appium import webdriver
import unittest
from PO.Android.DappVirtualCardPage import DAPPPage
from PO.basePage import Base
from PO.Android.usercenterPage import UsercenterPage
import time


class DappCase(unittest.TestCase):
    """
   DappCase界面的测试用例
    """

    def setUp(self):
        time.sleep(2)
        Base.android_driver_caps["noReset"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        # cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        # time.sleep(3)  # 等待初始化完成
        # cls.login_page.login_by_Email('sunge99@qq.com', 'Sunge123456') #调用登陆
        # cls.login_page.telegram_skip()  # 关闭telegram引导图
        self.Dapppage = DAPPPage(self.driver)
        self.usercenterPage = UsercenterPage(self.driver)
        time.sleep(10)

    def test_01_BTC_Receive(self):
        """
        点击查看BTC充值地址
        """
        self.Dapppage.click_BTC_Detail()
        time.sleep(3)
        self.Dapppage.Copy_Receive_Address()
        time.sleep(3)
        try:
            self.assertTrue(self.Dapppage.check_receive_code())
        except AssertionError:
            self.Dapppage.save_img("/BTC_Receive")

    def test_02_ETH_Receive(self):
        """
        点击查看ETH充值地址
        """
        self.Dapppage.click_ETH_Detail()
        time.sleep(3)
        self.Dapppage.Copy_Receive_Address()
        time.sleep(3)
        try:
            self.assertTrue(self.Dapppage.check_receive_code())
        except AssertionError:
            self.Dapppage.save_img("/ETH_Receive")

    def test_03_NPXS_Receive(self):
        """
        点击查看NPXS充值地址
        """
        self.Dapppage.click_NPXS_Detail()
        time.sleep(3)
        self.Dapppage.Copy_Receive_Address()
        time.sleep(3)
        try:
            self.assertTrue(self.Dapppage.check_receive_code())
        except AssertionError:
            self.Dapppage.save_img("/NPXS_Receive")

    def test_04_BNB_Receive(self):
        """
        点击查看BNB充值地址
        """
        self.Dapppage.click_BNB_Detail()
        time.sleep(3)
        self.Dapppage.Copy_Address_Memo()
        time.sleep(3)
        self.Dapppage.save_img("/BNB_Recevice")     # 保存BNB充值地址图片
        try:
            self.assertTrue(self.Dapppage.check_receive_code())
        except AssertionError:
            self.Dapppage.save_img("/BNB_Receive")

    def test_05_QTUM_Receive(self):
        """
        点击查看QTUM充值地址
        """
        self.Dapppage.click_QTUM_Detail()
        time.sleep(3)
        self.Dapppage.Copy_Receive_Address()
        time.sleep(3)
        try:
            self.assertTrue(self.Dapppage.check_receive_code())
        except AssertionError:
            self.Dapppage.save_img("/QTUM_Receive")

    def test_06_XEM_Receive(self):
        """点击查看XEM充值地址"""
        self.Dapppage.click_XEM_Detail()
        time.sleep(3)
        self.Dapppage.Copy_Address_Memo()
        self.Dapppage.save_img("/XEM_Recevice")  # 保存XEM充值地址图片

    def test_07_NPXSXEM_Recevice(self):
        """点击查看NPXSXEM充值地址"""
        self.Dapppage.click_NPXSXEM_Detail()
        time.sleep(5)
        self.Dapppage.click_NPXSXEM_Receice()
        self.Dapppage.save_img("/NPXSXEM_Recevice")  # 保存NPXSXEM充值地址图片
        time.sleep(5)


    def test_08_BTC_transfer(self):
        """BTC转账转全部"""
        self.Dapppage.click_BTC_Detail()
        time.sleep(2)
        self.Dapppage.Click_Transfer_without_Memo("n4mz19LnL84u4YQdNxX4V5kE6fwpyiMjcK")
        self.Dapppage.send_codes()
        self.Dapppage.confirm_transfer()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist('succee'))
            self.assertFalse(self.Dapppage.is_toast_exist('server'))
        except AssertionError:
            self.Dapppage.save_img('BTC_transfer')
        time.sleep(50)


    def test_09_ETH_transfer(self):
        """ETH转账"""
        self.Dapppage.click_ETH_Detail()
        time.sleep(2)
        self.Dapppage.Click_Transfer_without_Memo("0x4d7e60eab27597522232e04ab2743f14d903eeb5")
        self.Dapppage.send_codes()
        self.Dapppage.confirm_transfer()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succee"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("ETH_transfer")
        time.sleep(50)


    def test_10_NPXS_transfer(self):
        """NPXS转账"""
        self.Dapppage.click_NPXS_Detail()
        time.sleep(2)
        self.Dapppage.Click_Transfer_without_Memo("0x07a4a5ed9da97773e56dedcc0725e62efbcd61d1")
        self.Dapppage.send_codes()
        self.Dapppage.confirm_transfer()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succe"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("NPXS_transfer")

        time.sleep(50)

    def test_11_BNB_transfer(self):
        """BNB转账"""
        self.Dapppage.click_BNB_Detail()
        time.sleep(5)
        self.Dapppage.BEP2_transfer(address='tbnb1nlt0zerp80ysn9ve7guqstrshwd9cz3j9z8fzl', memo='4hw4977m6f', money='0.5')
        time.sleep(2)
        self.Dapppage.send_codes()
        self.Dapppage.confirm_transfer()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succe"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("BNB_transfer")

        time.sleep(50)

    def test_12_QTUM_transfer(self):
        """QTUM转账"""
        self.Dapppage.click_QTUM_Detail()
        time.sleep(2)
        self.Dapppage.Click_Transfer_without_Memo("qevcAgqD8rrJjaGutwQhDA1AT2FaXctdhm")
        time.sleep(2)
        self.Dapppage.send_codes()
        self.Dapppage.confirm_transfer()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succe"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("QTUM_transfer")
        time.sleep(50)

    def test_13_XEM_transfer(self):
        """XEM转账"""
        self.Dapppage.click_XEM_Detail()
        time.sleep(2)
        self.Dapppage.BEP2_transfer(address="TBF3ZZGCVY7NTWDABEH7P3KXD2LOYABEXASYDRUO",money='0.5')
        time.sleep(2)
        self.Dapppage.send_codes()
        self.Dapppage.confirm_transfer()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succe"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("XEM_transfer")
        time.sleep(50)

    def test_14_NPXSXEM_transfer(self):
        """NPXSXEM转账"""
        self.Dapppage.click_NPXSXEM_Detail()
        time.sleep(2)
        self.Dapppage.Click_NPXSXEM_Transfer()
        try:
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("NPXSXEM_transfer")

    def test_15_Internal_Transfer(self):
        """内部划转"""
        self.Dapppage.Internal_Transfer()
        time.sleep(2)
        self.usercenterPage.transfer_all()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)