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
        Base.android_driver_caps['noReset']=True
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
        if self.login_page.findElement("Skip"):
            self.login_page.click2('Skip')  # 登录成功后，点击红包引导界面的"跳过"按钮
            time.sleep(2)


        self.dapp_Page.enter_dapp()#点击Dapp按钮
        time.sleep(2)
        self.dapp_Page.add_fxcard()
        time.sleep(3)

    def test_002_click_fx_setting(self):
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

    def test_003_conversion(self):
        """
        进入conversion界面
        """
        #self.login_page.click2("Conversion")
        self.dapp_Page.click2(self.dapp_Page.fx_conversion_btn)
        time.sleep(4)
        self.driver.find_element_by_id(self.dapp_Page.conver_option_btn)
        time.sleep(2)

    def test_004_fx_transfer(self,address='0xd298500D22A49EE4BDf34330887ad3451fD5B510',amount='0.1',emailCode='2222',payPassword='123456'):
        """fx转账"""
        self.dapp_Page.Dapp_enter_fx()#点击DAPP界面的fx按钮
        self.dapp_Page.enter_fx()#点击fx卡片的fx按钮
        self.dapp_Page.fx_transfer(address,amount,emailCode,payPassword)#fx转账

    def test_005_fx_bill(self):
        """fx账单"""
        self.dapp_Page.Dapp_enter_fx()
        #msg=self.dapp_Page.enter_fx()
        #self.assertEqual(msg,u"FX Distribution")#前面加个u是转换字符串
        self.dapp_Page.enter_fx()

        #self.assertTrue("FX Distribution")
        self.assertTrue(self.dapp_Page.findElement("FX Distribution"))



    def test_006_npxs_help(self):
        """NPXS的帮助按钮"""
        self.dapp_Page.dapp_page()
        self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮

        self.assertTrue(self.dapp_Page.enter_NPXS_helpBtn())  # 点击帮助按钮
        self.dapp_Page.save_img('/006')
        # InsertLog().debug('1111')

    def test_007_npxs_changCard_position(self):
        self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮
        """切换NPXS卡片位置"""
        self.dapp_Page.click_transfer_exchange()

    def test_008_npxs_InterTransfer(self,amount='1'):
        """npxs的内部转账"""
        self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮
        self.dapp_Page.enter_NPXS_transfer()#点击转账按钮
        self.dapp_Page.input_Internal_transfer_amount()#转账操作

    def test_009_npxs_addChain(self,address='0xd298500D22A49EE4BDf34330887ad3451fD5B510',note='test1234'):
        """NPXS添加链上地址"""
        self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSPage()#点击fx卡片的npxs按钮
        self.dapp_Page.click_npxs_add()#点击ADD按钮
        self.dapp_Page.Add_NPXSchain_address(address,note)#输入链上地址以及备注


    def test_010_npxsxem_heleBtn(self):
        """点击npxsxem的帮助说明按钮"""
        self.dapp_Page.click_npxsxem_helpBtn()

    def test_011_npxsxem_receive(self):
        """测试npxsxem倒计时"""
        self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSXEMPage()#点击fx卡片的npxsxem按钮
        self.dapp_Page.click_npxsxem_viewBtn()#点击npxsxem界面的view按钮
        self.dapp_Page.click_npxsxem_receive()#点击npxsxem界面的received按钮
        self.dapp_Page.click_npxsxem_receiveCountdown()#点击npxsxem界面的倒计时、copy相关操作

    def test_012_npxsxem_transfer(self,npxsxem_address='TAZH6R4OUX3TOEXJCVU722JPMKLDBKPQ545XBV5O',amount='0.001',message='l4v2vizvev'):
        """测试npxsxem转账"""
        self.dapp_Page.Dapp_enter_fx() #点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSXEMPage()#点击fx卡片的npxsxem按钮
        self.dapp_Page.click_npxsxem_viewBtn()#点击view按钮
        self.dapp_Page.click_npxsxem_transfer()#点击npxsxem界面的转账按钮
        self.dapp_Page.npxsxem_transfer(npxsxem_address,amount,message)#npxsxem转账

    def test_013_npxsxem_addNem(self):
        """测试npxsxem添加链上地址"""

        self.dapp_Page.Dapp_enter_fx()  # 点击dapp界面的fx按钮
        self.dapp_Page.enter_NPXSXEMPage()  # 点击fx卡片的npxsxem按钮
        self.dapp_Page.click_npxsxem_add()#点击npxsxem界面的add按钮
        self.dapp_Page.add_npxsxem_chain_address()#添加npxsxem链上地址

    def test_014_staking_protocol(self):
        """测试进入协议"""
        self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
        self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
        self.dapp_Page.enter_staking_protocol()#进入挖矿的协议界面

    def test_015_staking_startMining(self):
        """测试开始挖矿"""
        self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
        self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
        self.assertFalse(self.dapp_Page.click_start_staking())

    def test_016_staking_history(self):
        """测试挖矿历史"""
        self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
        self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
        self.dapp_Page.click_staking_setting()#点击右上角的更多按钮
        self.dapp_Page.click_staking_history()#点击挖矿历史界面
        self.assertTrue(self.dapp_Page.findElement("Staking History"))#断言是否成功进入staking history界面

    def test_017_staking_shart(self):
        """测试挖矿分享"""
        self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
        self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
        self.dapp_Page.click_staking_setting()#点击右上角的更多按钮
        self.dapp_Page.click_staking_shareTo()#点击分享按钮
        self.assertTrue(self.dapp_Page.findElement("Share to"))#断言是否成功进入分享界面

    def test_018_staking_guide(self):
        """测试挖矿说明"""
        self.dapp_Page.Dapp_enter_fx()#点击dapp界面的fx按钮
        self.dapp_Page.enter_staking()#点击fx卡片的staking按钮
        self.dapp_Page.click_staking_setting()#点击右上角的更多按钮
        self.dapp_Page.click_staking_guide()#点击右上角的挖矿说明按钮
        self.assertTrue(self.dapp_Page.findElement("Staking Guide"))  # 断言是否成功进入说明界面界面

    def test_019_fresh_staking(self):
        """测试挖矿界面的下拉刷新"""
        self.dapp_Page.Dapp_enter_fx()  # 点击dapp界面的fx按钮
        self.dapp_Page.enter_staking()  # 点击fx卡片的staking按钮
        self.dapp_Page.fresh_staking()#下拉刷新

if __name__ == '__main__':
        unittest.main(verbosity=0)