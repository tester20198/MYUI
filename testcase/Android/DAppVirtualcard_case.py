from appium import webdriver
import unittest
from PO.Android.loginPage import LoginPage
from PO.Android.DappVirtualCardPage import DAPPPage
from PO.basePage import Base
import time


class ChatTestCase(unittest.TestCase):
    """
    Chat界面的测试用例
    """
    @classmethod
    def setUpClass(cls):
        Base.android_driver_caps["noReset"] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        time.sleep(3)  # 等待初始化完成
        cls.login_page.email_login('xgq1@xinjineng.net', 'Abc123456') #调用登陆
        cls.Dapppage = DAPPPage(cls.driver)

    def test_01_BTC_Receive(self):
        """
        点击查看BTC充值地址
        """
        self.Dapppage.click_Virtual_BTC()
        time.sleep(2)
        self.Dapppage.Copy_Receive_Address()
        try:
            self.assertTrue(self.Dapppage.check_receive_code())
        except AssertionError:
            self.Dapppage.save_img("/BTC_Receive")

    def test_02_ETH_Receive(self):
        """
        点击查看ETH充值地址
        """
        self.Dapppage.click_virtual_More()
        self.Dapppage.click_ETH_Detail()
        time.sleep(2)
        self.Dapppage.Copy_Receive_Address()
        try:
            self.assertTrue(self.Dapppage.check_receive_code())
        except AssertionError:
            self.Dapppage.save_img("/ETH_Receive")

    def test_03_NPXS_Receive(self):
        """
        点击查看NPXS充值地址
        """
        self.Dapppage.click_virtual_More()
        self.Dapppage.click_NPXS_Detail()
        time.sleep(2)
        self.Dapppage.Copy_Receive_Address()
        try:
            self.assertTrue(self.Dapppage.check_receive_code())
        except AssertionError:
            self.Dapppage.save_img("/NPXS_Receive")

    def test_04_BNB_Receive(self):
        """
        点击查看BNB充值地址
        """
        self.Dapppage.click_virtual_More()
        self.Dapppage.click_BNB_Detail()
        time.sleep(2)
        self.Dapppage.Copy_Address_Memo()
        self.Dapppage.save_img("/BNB_Recevice")     # 保存BNB充值地址图片
        self.Dapppage.driver.back()

    def test_05_QTUM_Receive(self):
        """
        点击查看QTUM充值地址
        """
        self.Dapppage.click_virtual_More()
        self.Dapppage.click_QTUM_Detail()
        time.sleep(2)
        self.Dapppage.Copy_Receive_Address()
        try:
            self.assertTrue(self.Dapppage.check_receive_code())
        except AssertionError:
            self.Dapppage.save_img("/QTUM_Receive")

    def test_06_XEM_Receive(self):
        """点击查看XEM充值地址"""
        self.Dapppage.click_virtual_More()
        self.Dapppage.click_XEM_Detail()
        time.sleep(2)
        self.Dapppage.Copy_Address_Memo()
        self.Dapppage.save_img("/XEM_Recevice")  # 保存XEM充值地址图片

    def test_07_NPXSXEM_Recevice(self):
        """点击查看NPXSXEM充值地址"""
        self.Dapppage.click_virtual_More()
        self.Dapppage.click_NPXSXEM_Detail()
        time.sleep(2)
        self.Dapppage.Copy_Address_Memo()
        self.Dapppage.save_img("/NPXSXEM_Recevice")  # 保存NPXSXEM充值地址图片

    def test_08_BTC_transfer(self):
        """BTC转账"""
        self.Dapppage.click_BTC_Detail()
        self.Dapppage.Click_Transfer_without_Memo("mxSDkQSmejdeKEKMkNnjQV9jHfwFTudg9v")
        self.Dapppage.Send_code()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist('succee'))
            self.assertFalse(self.Dapppage.is_toast_exist('server'))
        except AssertionError:
            self.Dapppage.save_img('BTC_transfer')

    def test_09_ETH_transfer(self):
        """ETH转账"""
        self.Dapppage.click_ETH_Detail()
        self.Dapppage.Click_Transfer_without_Memo("0xc9d83706efffc99896962cbb6025d67b2cb84b89")
        self.Dapppage.Send_code()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succee"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("ETH_transfer")

    def test_10_NPXS_transfer(self):
        """NPXS转账"""
        self.Dapppage.click_NPXS_Detail()

    def test_10_NPXS_transfer(self):
        """NPXS转账"""
        self.Dapppage.click_NPXS_Detail()
        self.Dapppage.Click_Transfer_without_Memo("0x2b9084c74e4406eb7c0e06c1df9bff2b2bf7bbdb")
        self.Dapppage.Send_code()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succe"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("NPXS_transfer")

    def test_11_BNB_transfer(self):
        """BNB转账"""
        self.Dapppage.click_BTC_Detail()
        self.Dapppage.Click_Transfer_with_memo("tbnb1x5n9ck6xhexwfjpxmp2ygg0ypndmrnfv9l45de")
        self.Dapppage.Send_code()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succe"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("BNB_transfer")

    def test_12_QTUM_transfer(self):
        """QTUM转账"""
        self.Dapppage.click_QTUM_Detail()
        self.Dapppage.Click_Transfer_without_Memo("qWMbKpZi3R5jtpcRP2aJxdWNJdGs2Z9L7W")
        self.Dapppage.Send_code()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succe"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("QTUM_transfer")

    def test_13_XEM_transfer(self):
        """XEM转账"""
        self.Dapppage.click_XEM_Detail()
        self.Dapppage.Click_Transfer_with_memo("TBF3ZZGCVY7NTWDABEH7P3KXD2LOYABEXASYDRUO")
        self.Dapppage.Send_code()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succe"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("XEM_transfer")

    def test_14_NPXSXEM_transfer(self):
        """NPXSXEM转账"""
        self.Dapppage.click_NPXSXEM_Detail()
        self.Dapppage.Click_Transfer_with_memo("TBF3ZZGCVY7NTWDABEH7P3KXD2LOYABEXASYDRUO")
        self.Dapppage.Send_code()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succe"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("NPXSXEM_transfer")

    def test_15_Internal_Transfer(self):
        """内部划转"""
        self.Dapppage.Internal_Transfer()
        try:
            self.assertTrue(self.Dapppage.is_toast_exist("succe"))
            self.assertFalse(self.Dapppage.is_toast_exist("server"))
        except AssertionError:
            self.Dapppage.save_img("Internal_Transfer")
