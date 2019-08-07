from appium import webdriver
import unittest
from PO.Android.loginPage import LoginPage
from PO.Android.DappVirtualCardPage import DAPPPage
from PO.basePage import Base
import time


class XPASSTestCase(unittest.TestCase):
    """
    XPASS卡的测试用例
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Base.android_driver_caps)  # 串联
        cls.login_page = LoginPage(cls.driver)  # 初始化登录页元素以及方法
        cls.login_page.check_in()
        time.sleep(1)
        cls.login_page.login_by_Email(' 476367003@xinjineng.net', 'Aa123456')
        time.sleep(5)
        cls.login_page.telegram_skip()  # 关闭telegram引导图
        cls.xpass_page = DAPPPage(cls.driver)  # 初始化个人中心页元素以及方法
        time.sleep(3)

    def test_001_check_add_XPASS(self):
        """添加XPASS"""

        self.xpass_page.add_XPASS_card(num='8011008881951290', pin='123456')
        self.assertTrue(self.xpass_page.is_toast_exist('already'), '判断是否提示已添加过该卡片')

    def test_002_check_XPASS_card(self):
        """检查XPASS细节"""

        self.driver.back()
        self.driver.back()
        self.driver.back()
        self.xpass_page.swipeDown()
        self.xpass_page.into_XPASS_card()
        time.sleep(2)
        self.xpass_page.click_card_setting()  # 卡片设置
        time.sleep(2)
        self.driver.back()
        self.xpass_page.click_card_bill()  # 卡片账单
        time.sleep(2)
        self.driver.back()
        self.xpass_page.click_card_eye()  # 卡片金额加密
        time.sleep(2)
        self.xpass_page.click_card_eye()  # 卡片金额加密

    def test_003_check_XPASS_BTC_rec(self, coin='NPXS'):
        """
        检查XPASS卡NPXS的充值地址
        coin：币种，根据币种改变测试用例
        """

        self.xpass_page.into_XPASS_card()
        time.sleep(2)
        self.xpass_page.into_coin_detail(coin)
        time.sleep(3)
        self.assertTrue(self.xpass_page.check_QR_code(), '判断付款二维码是否加啊在成功')
        time.sleep(1)
        self.xpass_page.click_refresh()  # 点击付款二维码刷新按钮
        time.sleep(2)
        try:
            self.xpass_page.check_card_Receive()  # 点击充值码并检查
            self.xpass_page.save_img(f'/{coin}充值码')
        except BaseException:
            print(f'无法获取{coin}充值二维码...')

    def test_004_check_XPASS_NPXS_transfer(self, coin='NPXS', address='16ERPgtkMD91tot9Q8HojfZLJzYt5GPYVV',
                                          money='0.00001'):
        """
        检查XPASS卡的NPXS的转账
        coin：币种，根据币种改变测试用例
        """

        self.driver.back()
        self.xpass_page.into_XPASS_card()
        time.sleep(2)
        self.xpass_page.into_coin_detail(coin)
        time.sleep(2)
        self.xpass_page.ERC20_transfer(address, money)  # 点击卡片中的转账
        time.sleep(2)
        self.xpass_page.send_codes(pwd='123123')  # 输入转账时的验证码
        time.sleep(1)
        self.xpass_page.confirm_transfer()
        self.assertTrue(self.xpass_page.is_toast_exist('transfer'), '判断是否转账成功')

    def test_005_XPASS_ETH_rec(self):
        """
        检查XPASS卡ETH的充值地址
        coin：币种，根据币种改变测试用例
        """

        self.test_003_check_XPASS_BTC_rec(coin='ETH')

    def test_006_check_XPASS_ETH_transfer(self):
        """
        检查XPASS卡的ETH的转账
        coin：币种，根据币种改变测试用例
        """

        self.test_004_check_XPASS_NPXS_transfer(coin='ETH', address='0xaA3A007c27F41B7527d339270b3c46EDAF51fe84', money='0.00001')

    def test_007_XPASS_BTC_rec(self):
        """
        检查XPASS卡BTC的充值地址
        coin：币种，根据币种改变测试用例
        """

        self.test_003_check_XPASS_BTC_rec(coin='BTC')

    def test_008_check_XPASS_BTC_transfer(self):
        """
        检查XPASS卡的BTC的转账
        coin：币种，根据币种改变测试用例
        """

        self.test_004_check_XPASS_NPXS_transfer(coin='BTC', address='0xaA3A007c27F41B7527d339270b3c46EDAF51fe84', money='0.00001')

    def test_009_check_XPASS_BNB_rec(self):
        """
        检查XPASS卡BNB的充值地址
        coin：币种，根据币种改变测试用例
        """

        self.driver.back()
        time.sleep(2)
        self.xpass_page.into_coin_detail(coin='BNB')
        time.sleep(2)
        try:
            self.xpass_page.Copy_Address_Memo()
            self.xpass_page.save_img('/BNB充值码截图')
        except BaseException:
            print(f'无法获取BNB充值二维码...')

    def test_010_check_XPASS_BNB_transfer(self):
        """检查XPASS卡的BNB的转账"""

        time.sleep(2)
        self.driver.back()
        time.sleep(1)
        self.xpass_page.BEP2_transfer(address='23423534543dfhhfghghjgf')
        time.sleep(1)
        self.xpass_page.send_codes()  # 输入转账时的验证码
        time.sleep(1)
        self.xpass_page.confirm_transfer()
        self.assertTrue(self.xpass_page.is_toast_exist('transfer'), '判断是否转账成功')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=0)
