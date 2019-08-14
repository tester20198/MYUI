from appium import webdriver
import unittest
from PO.Android.loginPage import LoginPage
from PO.Android.dappFxPage import DappFxPage
from Public.getLog import InsertLog
from PO.basePage import Base
from PO.basePage import Base
from selenium.webdriver.common.by import By
import time
from Public.getLog import write_log, stop_log
import time
import PO.Android.dappFxPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@unittest.skip
class DAppFxTestCase(unittest.TestCase):
    """
    DAPP的测试用例
    """

    @classmethod
    def setUpClass(cls):
        Base.android_driver_caps['noReset']= True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        cls.login_page = DappFxPage(cls.driver)  # 初始化登录页元素以及方法
        time.sleep(5)  # 等待初始化完成
        cls.dapp_Page=DappFxPage(cls.driver) #初始化dapp页的元素以及方法
        time.sleep(5)

    def test_001_add_FXCard(self):
        """点击添加卡片按钮"""
        try:
            if self.login_page.findElement("Skip"):
                self.login_page.click2('Skip')  # 登录成功后，点击红包引导界面的"跳过"按钮
                time.sleep(2)
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.add_fxcard()
            self.assertTrue(self.dapp_Page.findElement("Conversion"))
        except AssertionError:
            self.dapp_Page.save_img("/001_add_FXCard")
            raise AssertionError

    def test_002_click_fx_setting(self):
        """
        进入fx_setting
        """
        #self.login_page.click2("FX")
        try:
            self.dapp_Page.Dapp_notice()#如果存在紧急消息则打开
            self.dapp_Page.click2(self.dapp_Page.Dapp_enter_fx_card)#进入fx卡片
            time.sleep(2)
            self.dapp_Page.enter_fx_setting()
            time.sleep(2)
            self.assertTrue(self.dapp_Page.findElement("Card Settings"),'断言进入卡片设置界面')#断言进入卡片设置界面
            self.driver.back()
            time.sleep(2)
        except AssertionError:
            self.dapp_Page.save_img("/002_click_fx_setting")
            raise AssertionError

    def test_003_conversion(self):
        """
        进入conversion界面
        """
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.click_fx_text()  # 点击转换按钮
            self.dapp_Page.enter_conversion()# 点击帮助按钮
            time.sleep(4)
            self.assertTrue(self.dapp_Page.findElement("Instructions for f(x) token conversion"),'判断进入转换帮助界面')
            time.sleep(2)
        except AssertionError:
            self.dapp_Page.save_img("/003_conversion")
            raise AssertionError

    def test_004_fx_transfer(self,address='0xd298500D22A49EE4BDf34330887ad3451fD5B510',amount='0.1',emailCode='2222',payPassword='123456'):
        """
        测试fx转账
        :param address: fx转账地址
        :param amount: 转账金额
        :param emailCode: 邮箱验证码
        :param payPassword: 支付密码
        :return:
        """
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx()#点击DAPP界面的fx按钮
            self.dapp_Page.enter_fx()#点击fx卡片的fx按钮
            self.dapp_Page.fx_transfer(address,amount,emailCode,payPassword)#fx转账
            self.assertTrue(self.dapp_Page.is_toast_exist('Transfer successful'), '判断转账成功')
        except AssertionError:
            self.dapp_Page.save_img("/004_fx_transfer")
            raise AssertionError

    def test_005_fx_bill(self):
        """fx账单"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx()
        self.dapp_Page.enter_fx()

        try:
            fx_bill_count=self.driver.find_elements(*self.dapp_Page.fx_list)
            fx_bill_count[0].click()
            time.sleep(2)
        except AssertionError:
            self.dapp_Page.save_img("/005_fx_bill")
            raise AssertionError

    def test_006_npxs_help(self):
        """NPXS的帮助按钮"""
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.dapp_page()
            self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
            self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮
            self.assertTrue(self.dapp_Page.enter_NPXS_helpBtn(),"断言帮助界面")
        except AssertionError:
            self.dapp_Page.save_img('/007_npxs_help')
            raise AssertionError

    def test_007_npxs_changCard_position(self):
        """切换NPXS卡片位置"""
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
            self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮
            self.dapp_Page.enter_NPXS_transfer()#点击tranfer按钮
            self.dapp_Page.click_transfer_exchange()#点击内部划转的切换按钮
            self.assertTrue(self.dapp_Page.findElement("Internal Transfer"),'断言进入内部划转界面')
        except AssertionError:
            self.dapp_Page.save_img("/007_npxs_changCard_position")
            raise AssertionError

    def test_008_npxs_InterTransfer(self,amount='1'):
        """npxs的内部转账"""
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
            self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮
            self.dapp_Page.enter_NPXS_transfer()#点击转账按钮
            self.dapp_Page.input_Internal_transfer_amount(amount)#转账操作
            self.assertTrue(self.dapp_Page.is_toast_exist('Transfer successful' or 'Insufficient balance')) #'判断转账成功'
        except AssertionError:
            self.dapp_Page.save_img("/008_npxs_InterTransfer")
            raise AssertionError

    def test_009_npxs_addChain(self,address='0xd298500D22A49EE4BDf34330887ad3451fD5B510',note='12345'):
        """
        测试NPXS添加链上地址
        :param address: npxs链上地址
        :param note: 备注
        :return:
        """
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
            self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮
            self.dapp_Page.click_npxs_add()#点击ADD按钮
            self.dapp_Page.Add_NPXSchain_address(address,note)#输入链上地址以及备注
            self.assertTrue(self.dapp_Page.findElement("Transfer NPXS for verification"))
        except AssertionError:
            self.dapp_Page.save_img("/009_npxs_addChain")
            raise AssertionError

    def test_010_npxsxem_heleBtn(self):
        """点击npxsxem的帮助说明按钮"""
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
            self.dapp_Page.enter_NPXSXEMPage()#点击fx卡片的npxsxem按钮
            self.dapp_Page.click_npxsxem_helpBtn()
            self.assertTrue(self.dapp_Page.findElement("How to pair your NPXSXEM private wallet address with your XWallet Staking account?"))
        except AssertionError:
            self.dapp_Page.save_img("/010_npxsxem_heleBtn")
            raise AssertionError

    def test_011_npxsxem_receive(self):
        """测试npxsxem倒计时"""
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
            self.dapp_Page.enter_NPXSXEMPage()#点击fx卡片的npxsxem按钮
            self.dapp_Page.click_npxsxem_viewBtn()#点击npxsxem界面的view按钮
            self.dapp_Page.click_npxsxem_receive()#点击npxsxem界面的received按钮
            self.dapp_Page.click_npxsxem_receiveCountdown()#点击npxsxem界面的倒计时、copy相关操作
            self.assertTrue(self.dapp_Page.findElement("Copy Message"))
        except AssertionError:
            self.dapp_Page.save_img("/011_npxsxem_receive")
            raise AssertionError

    def test_012_npxsxem_transfer(self,npxsxem_address='TAZH6R4OUX3TOEXJCVU722JPMKLDBKPQ545XBV5O',amount='0.1',message='l4v2vizvev',email_code='2222',payPassword='123456'):
        """
        测试npxsxem转账
        :param npxsxem_address: npxsxem转账地址
        :param amount: 转账金额
        :param message: 转账附言
        :return:
        """
        try:

            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
            self.dapp_Page.enter_NPXSXEMPage()#点击fx卡片的npxsxem按钮
            self.dapp_Page.click_npxsxem_viewBtn()#点击view按钮
            self.dapp_Page.click_npxsxem_transfer()#点击npxsxem界面的转账按钮
            self.dapp_Page.npxsxem_transfer(npxsxem_address,amount,message,email_code,payPassword)#npxsxem转账
            self.assertTrue(self.dapp_Page.is_toast_exist('Transfer successful' or 'Insufficient balance'))  # '判断转账成功'
        except AssertionError:
            self.dapp_Page.save_img("/012_npxsxem_transfer")
            raise AssertionError

    def test_013_npxsxem_addNPXSXem(self):
        """测试npxsxem添加链上地址"""
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx()  # 点击dapp界面的fx按钮
            self.dapp_Page.enter_NPXSXEMPage()  # 点击fx卡片的npxsxem按钮
            self.dapp_Page.click_npxsxem_add()#点击npxsxem界面的add按钮
            self.dapp_Page.add_npxsxem_chain_address()#添加npxsxem链上地址
        except AssertionError:
            self.dapp_Page.save_img("/013_npxsxem_addNPXSXem")
            raise AssertionError

    def test_014_staking_protocol(self):
        """测试进入协议"""
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
            self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
            self.dapp_Page.enter_staking_protocol()#进入挖矿的协议界面
        except AssertionError:
            self.dapp_Page.save_img("/014_staking_protocol")
            raise AssertionError

    def test_015_staking_startMining(self):
        """测试开始挖矿"""

        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
            self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
            #self.dapp_Page.switch_to_view()  # 切换到h5界面
            self.dapp_Page.click_start_staking()#点击开始挖矿按钮
            if self.dapp_Page.findElement("Staking"):
                print("点击开始挖矿按钮成功")
                pass
            elif self.dapp_Page.findElement("Total amount"):
                print("点击提现的下一步按钮成功")
                pass
            #self.assertTrue(self.dapp_Page.findElement("Staking" or "Withdraw"))
        except AssertionError:
            self.dapp_Page.save_img("/015_staking_startMining")
            raise AssertionError

    def test_016_staking_history(self):
        """测试挖矿历史"""
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
            self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
            self.dapp_Page.click_staking_setting()#点击右上角的更多按钮
            self.dapp_Page.click_staking_history()#点击挖矿历史界面
        except AssertionError:
            self.dapp_Page.save_img("/016_staking_history")
            raise AssertionError

    def test_017_staking_shareTo(self):
        """测试挖矿分享"""
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
            self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
            self.dapp_Page.click_staking_setting()#点击右上角的更多按钮
            self.dapp_Page.click_staking_shareTo()#点击分享按钮
            self.assertTrue(self.dapp_Page.findElement("Share to"))#断言是否成功进入分享界面
        except AssertionError:
            self.dapp_Page.save_img("/017_staking_shareTo")
            raise AssertionError

    def test_018_staking_guide(self):
        """测试挖矿说明"""
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
            self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
            self.dapp_Page.click_staking_setting()#点击右上角的更多按钮
            self.dapp_Page.click_staking_guide()#点击右上角的挖矿说明按钮
            self.assertTrue(self.dapp_Page.findElement("Staking Guide"))  # 断言是否成功进入说明界面界面
        except AssertionError:
            self.dapp_Page.save_img("/018_staking_guide")
            raise AssertionError

    def test_019_fresh_staking(self):
        """测试挖矿界面的下拉刷新"""
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx()  # 点击dapp界面的fx按钮
            self.dapp_Page.enter_staking()  # 点击fx卡片的staking按钮
            self.dapp_Page.fresh_staking()#下拉刷新
        except AssertionError:
            self.dapp_Page.save_img("/019_fresh_staking")
            raise AssertionError

    def test_020_npxsxem_list(self,address='112233'):
        """
        测试npxsxem界面的列表数据
        :param address: address note
        :return:
        """
        try:
            self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
            self.dapp_Page.Dapp_enter_fx()  # 点击dapp界面的fx按钮
            self.dapp_Page.enter_NPXSXEMPage()  # 点击fx卡片的npxsxem按钮
            msg,msg1 = self.dapp_Page.click_tv_private_account(address) #调用npxsxem列表的方法
            self.assertListEqual([msg,msg1],[address,address]) #断言2个值相等
        except (BaseException,AssertionError):
            self.dapp_Page.save_img("/020_npxsxem_list_fail")
            raise AssertionError


if __name__ == '__main__':
        unittest.main(verbosity=0)