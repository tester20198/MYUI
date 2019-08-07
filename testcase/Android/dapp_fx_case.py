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




    def test_001_add_FXCard(self):
        """点击添加卡片按钮"""

        while self.login_page.findElement("Skip"):
            self.login_page.click2('Skip')  # 登录成功后，点击红包引导界面的"跳过"按钮
            time.sleep(2)

        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.add_fxcard()
        self.assertTrue(self.dapp_Page.findElement("Conversion"))
        self.dapp_Page.save_img("/001_add_FXCard")

    def test_002_click_fx_setting(self):
        """
        进入fx_setting
        """
        #self.login_page.click2("FX")
        self.dapp_Page.Dapp_notice()#如果存在紧急消息则打开
        self.dapp_Page.click2(self.dapp_Page.Dapp_enter_fx_card)#进入fx卡片
        time.sleep(2)
        self.dapp_Page.enter_fx_setting()
        time.sleep(2)
        self.assertTrue(self.dapp_Page.findElement("Card Settings"),'断言进入卡片设置界面')#断言进入卡片设置界面
        self.driver.back()
        time.sleep(2)
        self.dapp_Page.save_img("/002_click_fx_setting")

    def test_003_conversion(self):
        """
        进入conversion界面
        """
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.click_fx_text()  # 点击转换按钮
        self.dapp_Page.enter_conversion()# 点击帮助按钮
        time.sleep(4)
        self.assertTrue(self.dapp_Page.findElement("Instructions for f(x) token conversion"),'判断进入转换帮助界面')
        time.sleep(2)
        self.dapp_Page.save_img("/003_conversion")

    def test_004_fx_transfer(self,address='0xd298500D22A49EE4BDf34330887ad3451fD5B510',amount='0.1',emailCode='2222',payPassword='123456'):
        """
        测试fx转账
        :param address: fx转账地址
        :param amount: 转账金额
        :param emailCode: 邮箱验证码
        :param payPassword: 支付密码
        :return:
        """
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx()#点击DAPP界面的fx按钮
        self.dapp_Page.enter_fx()#点击fx卡片的fx按钮
        self.dapp_Page.fx_transfer(address,amount,emailCode,payPassword)#fx转账
        self.assertTrue(self.dapp_Page.is_toast_exist('Transfer successful'), '判断转账成功')
        self.dapp_Page.save_img("/004_fx_transfer")

    def test_005_fx_bill(self):
        """fx账单"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx()
        self.dapp_Page.enter_fx()


        fx_bill_count=self.driver.find_elements(*self.dapp_Page.fx_list)
        # transfer_type = self.driver.find_element(*self.dapp_Page.fx_transfer_type)
        # fx_distribution = self.driver.find_element(*self.dapp_Page.fx_FX_Distribution)
        # staking_bill = self.driver.find_element(*self.dapp_Page.fx_Allocation_from_Staking)

        fx_bill_count[0].click()
        time.sleep(2)
        self.dapp_Page.save_img("/005_fx_bill")
        # for i in fx_bill_count:
        #
        #     if transfer_type:
        #         print(transfer_type + "111111")
        #         transfer_type.click()
        #         time.sleep(2)
        #         self.dapp_Page.findElement("Transfer", '进入转账界面')
        #     elif staking_bill:
        #         print(staking_bill + "22222")
        #         staking_bill.click()
        #         time.sleep(2)
        #         self.dapp_Page.findElement("Allocation from Staking", '进入挖矿账单')
        #     elif fx_distribution:
        #         fx_distribution.click()
        #         time.sleep(2)
        #         self.dapp_Page.findElement("FX Distribution", "fx兑换")
        #     self.assertTrue(self.dapp_Page.findElement("FX"),'判断是否进入fx账单')

    def test_006_npxs_help(self):
        """NPXS的帮助按钮"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.dapp_page()
        self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮

        self.assertTrue(self.dapp_Page.enter_NPXS_helpBtn(),"断言帮助界面")
        self.dapp_Page.save_img('/007')
        # InsertLog().debug('1111')

    def test_007_npxs_changCard_position(self):
        """切换NPXS卡片位置"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮
        self.dapp_Page.enter_NPXS_transfer()#点击tranfer按钮
        self.dapp_Page.click_transfer_exchange()#点击内部划转的切换按钮
        self.assertTrue(self.dapp_Page.findElement("Internal Transfer"),'断言进入内部划转界面')
        self.dapp_Page.save_img("/007_npxs_changCard_position")

    def test_008_npxs_InterTransfer(self,amount='1'):
        """npxs的内部转账"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮
        self.dapp_Page.enter_NPXS_transfer()#点击转账按钮
        self.dapp_Page.input_Internal_transfer_amount(amount)#转账操作
        self.assertTrue(self.dapp_Page.is_toast_exist('Transfer successful' or 'Insufficient balance')) #'判断转账成功'
        self.dapp_Page.save_img("/008_npxs_InterTransfer")

    def test_009_npxs_addChain(self,address='0xd298500D22A49EE4BDf34330887ad3451fD5B510',note='12345'):
        """
        测试NPXS添加链上地址
        :param address: npxs链上地址
        :param note: 备注
        :return:
        """
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮
        self.dapp_Page.click_npxs_add()#点击ADD按钮
        self.dapp_Page.Add_NPXSchain_address(address,note)#输入链上地址以及备注
        self.assertTrue(self.dapp_Page.findElement("Transfer NPXS for verification"))
        self.dapp_Page.save_img("/009_npxs_addChain")


    def test_010_npxsxem_heleBtn(self):
        """点击npxsxem的帮助说明按钮"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSXEMPage()#点击fx卡片的npxsxem按钮
        self.dapp_Page.click_npxsxem_helpBtn()
        self.assertTrue(self.dapp_Page.findElement("How to pair your NPXSXEM private wallet address with your XWallet Staking account?"))
        self.dapp_Page.save_img("/010_npxsxem_heleBtn")

    def test_011_npxsxem_receive(self):
        """测试npxsxem倒计时"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSXEMPage()#点击fx卡片的npxsxem按钮
        self.dapp_Page.click_npxsxem_viewBtn()#点击npxsxem界面的view按钮
        self.dapp_Page.click_npxsxem_receive()#点击npxsxem界面的received按钮
        self.dapp_Page.click_npxsxem_receiveCountdown()#点击npxsxem界面的倒计时、copy相关操作
        self.assertTrue(self.dapp_Page.findElement("Copy Message"))
        self.dapp_Page.save_img("/011_npxsxem_receive")

    def test_012_npxsxem_transfer(self,npxsxem_address='TAZH6R4OUX3TOEXJCVU722JPMKLDBKPQ545XBV5O',amount='0.1',message='l4v2vizvev',email_code='2222',payPassword='123456'):
        """
        测试npxsxem转账
        :param npxsxem_address: npxsxem转账地址
        :param amount: 转账金额
        :param message: 转账附言
        :return:
        """

        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSXEMPage()#点击fx卡片的npxsxem按钮
        self.dapp_Page.click_npxsxem_viewBtn()#点击view按钮
        self.dapp_Page.click_npxsxem_transfer()#点击npxsxem界面的转账按钮
        self.dapp_Page.npxsxem_transfer(npxsxem_address,amount,message,email_code,payPassword)#npxsxem转账
        self.assertTrue(self.dapp_Page.is_toast_exist('Transfer successful' or 'Insufficient balance'))  # '判断转账成功'
        self.dapp_Page.save_img("/012_npxsxem_transfer")

    def test_013_npxsxem_addNPXSXem(self):
        """测试npxsxem添加链上地址"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx()  # 点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSXEMPage()  # 点击fx卡片的npxsxem按钮
        self.dapp_Page.click_npxsxem_add()#点击npxsxem界面的add按钮
        self.dapp_Page.add_npxsxem_chain_address()#添加npxsxem链上地址
        self.dapp_Page.save_img("/013_npxsxem_addNPXSXem")

    def test_014_staking_protocol(self):
        """测试进入协议"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
        self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
        self.dapp_Page.enter_staking_protocol()#进入挖矿的协议界面
        self.dapp_Page.save_img("/014_staking_protocol")

    def test_015_staking_startMining(self):
        """测试开始挖矿"""
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
        self.dapp_Page.save_img("/015_staking_startMining")

    def test_016_staking_history(self):
        """测试挖矿历史"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
        self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
        self.dapp_Page.click_staking_setting()#点击右上角的更多按钮
        self.dapp_Page.click_staking_history()#点击挖矿历史界面
        self.dapp_Page.save_img("/016_staking_history")

    def test_017_staking_shareTo(self):
        """测试挖矿分享"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
        self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
        self.dapp_Page.click_staking_setting()#点击右上角的更多按钮
        self.dapp_Page.click_staking_shareTo()#点击分享按钮
        self.assertTrue(self.dapp_Page.findElement("Share to"))#断言是否成功进入分享界面
        self.dapp_Page.save_img("/017_staking_shareTo")

    def test_018_staking_guide(self):
        """测试挖矿说明"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
        self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
        self.dapp_Page.click_staking_setting()#点击右上角的更多按钮
        self.dapp_Page.click_staking_guide()#点击右上角的挖矿说明按钮
        self.assertTrue(self.dapp_Page.findElement("Staking Guide"))  # 断言是否成功进入说明界面界面
        self.dapp_Page.save_img("/018_staking_guide")

    def test_019_fresh_staking(self):
        """测试挖矿界面的下拉刷新"""
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx()  # 点击dapp界面的fx按钮
        self.dapp_Page.enter_staking()  # 点击fx卡片的staking按钮
        self.dapp_Page.fresh_staking()#下拉刷新
        self.dapp_Page.save_img("/019_fresh_staking")

    def test_020_npxsxem_list(self,address='112233'):
        """
        测试npxsxem界面的列表数据
        :param address: address note
        :return:
        """
        self.dapp_Page.Dapp_notice()  # 如果存在紧急消息则打开
        self.dapp_Page.Dapp_enter_fx()  # 点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSXEMPage()  # 点击fx卡片的npxsxem按钮
        msg = self.dapp_Page.click_tv_private_account(address)#调用npxsxem列表的方法
        self.assertEqual(msg,address)#断言2个值相等



if __name__ == '__main__':
        unittest.main(verbosity=0)