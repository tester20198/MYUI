from appium import webdriver
import unittest
from Public.getLog import InsertLog
from PO.Android.DappOpenCardPage import DappOpenCardPage
from PO.basePage import Base
import time

class DappOpenCardTestCase(unittest.TestCase):
    """
    Dapp-开放平台卡片 测试用例
    """
    @classmethod
    def setUpClass(cls):
        Base.android_driver_caps["noReset"] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        # cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        time.sleep(3)  # 等待初始化完成
        # cls.login_page.email_login('xgq1@xinjineng.net', 'Abc123456') #调用登陆
        cls.open_page = DappOpenCardPage(cls.driver)

    def test_001_add_open_platform_Virtual_Card(self,type=u'Virtual Card'):
        '''
        用例一: 添加开放平台虚拟卡
        :param type: 添加的卡片类型
        :return:
        '''
        try:
            self.open_page.dapp_page() #点击dapp菜单
            time.sleep(1)
            self.open_page.add_card_buisess(type)
            msg = self.open_page.add_virtual_card()
            self.assertTrue(msg)
            print('添加虚拟卡,获取的页面的标题信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            self.open_page.save_img("/Virtual_card")
            InsertLog().debug(msg)
            raise BaseException

    def test_002_add_open_platform_Physical_Card(self,type=u'Physical Card',cardmunber='1111111111111111',pwd='123456'):
        '''
        用例二: 添加开放平台实体卡
        :param type: 添加的卡片类型
        :param cardmunber: 卡号
        :param pwd: 卡密码
        :return:
        '''
        try:
            self.open_page.dapp_page() #点击dapp菜单
            time.sleep(1)
            self.open_page.add_card_buisess(type)
            self.assertTrue(self.open_page.add_physical_card(cardmunber,pwd))
        except (BaseException, AssertionError) as msg:
            self.open_page.save_img("/Physical_card")
            InsertLog().debug(msg)
            raise BaseException

    def test_003_Card_details(self):
        '''
        用例三: 卡片详情界面加密、设置按钮、账单
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            msg, msg1= self.open_page.card_details_page()
            # msg = Card Settings;msg1 = Transactions
            self.assertListEqual([msg, msg1], ['Card Settings', 'Transactions'])
        except (BaseException, AssertionError) as msg:
            self.open_page.save_img("/Card_details")
            InsertLog().debug(msg)
            raise BaseException

    def test_004_Receive_address(self):
        '''
        用例四: 查看充值地址
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.open_page.check_receive_address()
            self.assertTrue(self.open_page.check_receive_address()) #二维码可用则通过
        except (BaseException, AssertionError) as msg:
            self.open_page.save_img("/open_receive_address")
            InsertLog().debug(msg)
            raise BaseException

    def test_005_Transfer_buisess(self,address='0x6cb73a52eae9ab40edb6c6d0f912192306f08278',amount='0.1',code='2222',pwd='123456'):
        '''
        用例五: 转账流程
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.assertTrue(self.open_page.transfer_buisess(address,amount,code,pwd))
        except (BaseException, AssertionError) as msg:
            self.open_page.save_img("/Transfer_fail")
            InsertLog().debug(msg)
            raise BaseException

    def test_006_Receive_address(self):
        '''
        用例六: 付款二维码
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.open_page.click_pay_button()
            self.assertTrue(self.open_page.check_receive_code()) #二维码可用则通过
        except (BaseException, AssertionError) as msg:
            self.open_page.save_img("/Payment_code")
            InsertLog().debug(msg)
            raise BaseException

    def test_007_Receive_address(self):
        '''
        用例六: 付款二维码
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.open_page.click_pay_button()
            self.assertFalse(self.open_page.check_receive_code()) #二维码可用则通过
        except (BaseException, AssertionError) as msg:
            self.open_page.save_img("/Payment_code")
            InsertLog().debug(msg)
            raise BaseException


    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)