from appium import webdriver
import unittest
from PO.Android.DappOpenCardPage import DappOpenCardPage
from PO.basePage import Base
import time


class DappOpenCardTestCase(unittest.TestCase):
    """
    Dapp-开放平台卡片 测试用例
    """

    def setUp(self):
        self.cardname = u'KMD'  # 必须传参开放平台卡片名称
        Base.android_driver_caps["noReset"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        # self.login_page = LoginPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(3)  # 等待初始化完成
        # self.login_page.check_in()
        # self.login_page.login_by_Email('xgq2@xinjineng.net', 'Abc123456')  # 调用登陆
        self.open_page = DappOpenCardPage(self.driver)

    def test_001_add_open_platform_Virtual_Card(self):
        '''
        用例一: 添加开放平台虚拟卡
        :param type: 添加的卡片类型
        :return:
        '''
        try:
            self.open_page.dapp_page() #点击dapp菜单
            time.sleep(1)
            self.open_page.add_card_buisess(self.cardname)
            self.open_page.add_virtual_card() #判断添加成功
        except (BaseException, AssertionError):
            self.open_page.save_img("/001_Open_Virtual_card_fail")
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
        except (BaseException, AssertionError):
            self.open_page.save_img("/002_Physical_card_fail")
            raise BaseException

    def test_003_Card_details(self):
        '''
        用例三: 卡片详情界面加密、设置按钮、账单、开发者网站
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            msg,msg1,msg2= self.open_page.card_details_page(self.cardname)
            # msg = Card Settings;msg1 = Transactions
            self.assertListEqual([msg, msg1,msg2], ['Card Settings', 'Transactions',self.cardname])
        except (BaseException, AssertionError):
            self.open_page.save_img("/003_Card_details_fail")
            raise BaseException

    def test_004_Receive_address(self):
        '''
        用例四: 查看充值地址
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.open_page.card_details(self.cardname)
            self.assertTrue(self.open_page.check_receive_address()) #二维码可用则通过
        except (BaseException, AssertionError):
            self.open_page.save_img("/004_Receive_address_fail")
            raise BaseException

    def test_005_Transfer_buisess(self,address='0x6cb73a52eae9ab40edb6c6d0f912192306f08278',amount='0.1',code='2222',pwd='123456'):
        '''
        用例五: 转账流程
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.open_page.card_details(self.cardname)
            self.assertTrue(self.open_page.transfer_buisess(address,amount,code,pwd,self.cardname))
        except (BaseException, AssertionError):
            self.open_page.save_img("/005_Transfer_fail")
            raise BaseException

    def test_006_Payment_Code(self):
        '''
        用例六: 付款二维码
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.open_page.card_details(self.cardname)
            self.assertTrue(self.open_page.check_receive_code()) #二维码可用则通过
        except (BaseException, AssertionError):
            self.open_page.save_img("/006_Payment_code_fail")
            raise BaseException

    def test_007_Hlep_And_Cancel(self):
        '''
        用例七: 帮助说明、取消功能
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.open_page.card_details(self.cardname)
            self.assertTrue(self.open_page.click_help())
        except (BaseException, AssertionError):
            self.open_page.save_img("/007_help_and_cancel_fail")
            raise BaseException

    def test_008_Internal_Transfer(self):
        '''
        用例八: 内部划转
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.open_page.card_details(self.cardname)
            self.assertTrue(self.open_page.Internal_Transfer())
        except (BaseException, AssertionError):
            self.open_page.save_img("/008_Internal_Transfer_fail")
            raise BaseException

    def test_009_Transaction_History(self):
        '''
        用例九: 账单记录
        '''
        try:
            self.open_page.dapp_page()  # 点击dapp菜单
            time.sleep(1)
            self.open_page.card_details(self.cardname)
            self.open_page.Transaction_history()
        except (BaseException, AssertionError):
            self.open_page.save_img("/009_Transaction_history_fail")
            raise BaseException

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)